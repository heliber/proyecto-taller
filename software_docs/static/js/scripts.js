document.querySelector('.menu-item > a').addEventListener('click', function(event) {
    event.preventDefault(); // Evita que el enlace recargue la página
    const submenu = this.nextElementSibling;
    if (submenu.style.display === 'block') {
        submenu.style.display = 'none';
        this.innerHTML = 'Documentación de Artefactos &#x25B2;';
    } else {
        submenu.style.display = 'block';
        this.innerHTML = 'Documentación de Artefactos &#x25BC;';
    }
});
