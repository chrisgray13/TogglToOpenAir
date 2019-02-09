from DailyTimeEntryExtensions import getDay, getDayOfTheWeek, roundDuration

class OpenAirTimesheetPopulator:
    def generateTimesheetPopulationScript(self, data):
        script = """\
(function () {
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
"""

        row = 1

        for projectEntries in data:
            script += "\n"

            for entry in projectEntries.values():
                script += "    addHours({0}, {1}, {2}, {3}, '{4}');\n".format(row, getDayOfTheWeek(entry.date, 7), getDay(entry.date), roundDuration(entry.duration), entry.description.replace("'", "\\'"))

            script += "    setTaskInfo({0}, '{1}', '{2}', '{3}');\n".format(row, entry.client.replace("'", "\\'"), entry.project.replace("'", "\\'"), "Non-Billable")
            row += 1

        script += "})();"

        return script