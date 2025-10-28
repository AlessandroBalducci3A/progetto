document.addEventListener("DOMContentLoaded", () => {
  const bottone = document.getElementById("vaiPagina");

  bottone.addEventListener("click", () => {
    // Quando clicchi, vai alla nuova pagina
    window.location.href = "pagina2.html";
  });
});