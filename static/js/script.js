/* jshint esversion: 11, jquery: true */
document.addEventListener('DOMContentLoaded', function () {
    // mobile sidebar
    let sidenavs = document.querySelectorAll(".sidenav");
    let sidenavsInstance = M.Sidenav.init(sidenavs, {
        edge: "right"
    });

    // date picker initialization
    let datePickers = document.querySelectorAll('.datepicker');
    let datePickerInstances = M.Datepicker.init(datePickers, {
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });

     // time picker initialization
     let timePickers = document.querySelectorAll('.timepicker');
     let timePickerInstances = M.Timepicker.init(timePickers, {
       
         showClearBtn: true,
         i18n: {
             done: "Select",
             cancel: "cancel",
             clear: "clear",
         }
     });
    let modals = document.querySelectorAll('.modal');
    let modalInstances = M.Modal.init(modals, {});

});