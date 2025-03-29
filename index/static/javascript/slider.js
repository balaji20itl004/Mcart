document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".slider");
    let index = 0;

    function slide() {
        index++;
        if (index >= slider.children.length) {
            index = 0;
        }
        slider.style.transform = `translateX(-${index * 100}%)`;
    }

    setInterval(slide, 3000); 
});
