const form = document.querySelector(".form");
const spinner = document.querySelector(".lds-ring")
const button = document.querySelector(".form__btn")


form.addEventListener("submit", (e) => {
    // e.preventDefault();
    spinner.classList.remove("hidden")
    button.classList.add("hidden")
})