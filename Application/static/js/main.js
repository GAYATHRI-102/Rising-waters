document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("predictionForm");

    if (form) {

        form.addEventListener("submit", function (event) {

            const inputs = form.querySelectorAll("input");

            for (let input of inputs) {

                if (input.value.trim() === "") {
                    alert("Please fill all the fields.");
                    input.focus();
                    event.preventDefault();
                    return;
                }

                if (isNaN(input.value)) {
                    alert("Please enter only numeric values.");
                    input.focus();
                    event.preventDefault();
                    return;
                }
            }

        });

    }

});