document.addEventListener('DOMContentLoaded', function () {
        let sidenavs = document.querySelectorAll(".sidenav");
        let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});

        var elems = document.querySelectorAll('.datepicker');
        var instances = M.Datepicker.init(elems, {
            format: "dd mmmm, yyyy",
            yearRange: 3,
            showClearBtn: true,
            i18n: {
                done: "Select"
            }
        });
    });