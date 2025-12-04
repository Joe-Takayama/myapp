document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".image-grid .item");
    const modal = document.getElementById("modal");
    const closeBtn = document.querySelector(".close-btn");

    const modalImage = document.getElementById("modal-image");
    const modalTitle = document.getElementById("modal-title");
    const modalDate = document.getElementById("modal-date");
    const modalRelease = document.getElementById("modal-release");
    const modalCharacters = document.getElementById("modal-characters");
    const modalStory = document.getElementById("modal-story");

    items.forEach(item => {
        item.addEventListener("click", () => {

            modalImage.src = item.querySelector("img").src;

            modalTitle.textContent = item.dataset.title;
            modalDate.textContent = `作中の日付：${item.dataset.date}`;
            modalRelease.textContent = `発売日：${item.dataset.release}`;
            modalCharacters.textContent = `主要人物：${item.dataset.characters}`;
            modalStory.textContent = item.dataset.story;

            modal.style.display = "flex";
        });
    });

    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    modal.addEventListener("click", (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });
});
