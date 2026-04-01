var cityList = document.querySelectorAll(".city-list li a");
cityList.forEach((city) => {
    city.addEventListener("click", function () {
        alert("Loading weather report...")
    })
});

var foot = document.querySelector(".footer");
var acceptBtn = document.querySelector(".btn");
acceptBtn.addEventListener("click", function () {
    foot.remove();
})

var select = document.querySelector(".select-tmp");
var temperatures = document.querySelectorAll(".h3-first, .h3-sec");

select.addEventListener("change", function () {
    var unit = select.value;

    temperatures.forEach((tempElement) => {
        var currentTemp = parseInt(tempElement.innerText);
        var newTemp = 0;

        if (unit === "°F") {
            newTemp = Math.round((currentTemp * 9 / 5) + 32);
            tempElement.innerText = newTemp + "°";
        } else {
            newTemp = Math.round((currentTemp - 32) * 5 / 9);
            tempElement.innerText = newTemp + "°";
        }
    });
});
