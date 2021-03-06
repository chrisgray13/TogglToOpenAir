from DailyTimeEntryExtensions import getDay, getDayOfTheWeek, roundDuration

class OpenAirTimesheetPopulator:
    def generateTimesheetPopulationScript(self, data):
        script = """\
(function () {
    $("body").append("<div id=\\"loadingImage\\" style=\\"background: #3F3F3F;width: 100%;height: 100%;position: absolute;top: 0px;left: 0px;z-index: 10000;opacity: .8;text-align: center;\\"><span style=\\"font-size: 20em;color: #000000;padding: 20px;\\">Loading</span></div>");
})();

setTimeout(function() {
    function setTaskInfo(row, project, task, timeType) {
        // Set the Project
        var ctrl = $('#ts_c1_r' + row);
        ctrl.children('option:contains("' + project + '")').prop('selected', 'selected');
        ctrl.trigger('change');
        // Set the Task
        ctrl = $('#ts_c2_r' + row);
        ctrl.children('option:contains("' + task + '")').prop('selected', 'selected');
        ctrl.trigger('change');
        // Set the Time type
        ctrl = $('#ts_c3_r' + row);
        ctrl.children('option:contains("' + timeType + '")').prop('selected', 'selected');
        ctrl.trigger('change');
    }

    function addHours(row, dayOfWeek, day, hours, description) {
        var dateColumn = dayOfWeek + 3;
        if ($('th.timesheetFixedColumn' + (11 - dateColumn) + ':first span.monthDay').text() == day) {
            $('#ts_c' + dateColumn + '_r' + row).val(hours).trigger('change');
            // Pop the modal
            $('#ts_notes_c' + dateColumn + '_r' + row).click();
            // Set the description
            $('#tm_desc').val(description);
            // Click the OK button
            $('.btn-oa.dialogOkButton').click();
        }
    }

    var lastRow = $("tr.gridDataEmptyRow select")[0];
    var row = lastRow === undefined ? 1 : parseInt(lastRow.id.slice(7));
"""

        for projectEntries in data:
            script += "\n"

            for entry in projectEntries.values():
                roundedDuration = roundDuration(entry.duration)
                if roundedDuration <= 0.0:
                    script += "    // Skipping =>"

                script += "    addHours(row, {0}, {1}, {2}, '{3}');\n".format(getDayOfTheWeek(entry.date, 7), getDay(entry.date), roundedDuration, entry.description.replace("'", "\\'"))

            script += "    setTaskInfo(row++, '{0}', '{1}', '{2}');\n".format(entry.client.replace("'", "\\'"), entry.project.replace("'", "\\'"), "Non-Billable")

        script += """
    $(\"body #loadingImage\").remove();
}, 1000);"""

        return script
