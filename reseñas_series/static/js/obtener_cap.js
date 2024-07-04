document.addEventListener('DOMContentLoaded', function() {
    var serieField = document.querySelector('select[name="serie"]');
    var capituloField = document.querySelector('select[name="capitulo"]');

    serieField.addEventListener('change', function() {
        var serieId = this.value;
        var url = '/reseñas/obtener_episodios/?serie_id=' + serieId;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Limpiar el campo de episodios
                capituloField.innerHTML = '';
                // Agregar la opción "Seleccione un capítulo"
                var option = document.createElement('option');
                option.value = '';
                option.text = 'Seleccione un capítulo';
                capituloField.appendChild(option);
                
                // Rellenar con nuevas opciones
                data.forEach(function(ep) {
                    var option = document.createElement('option');
                    option.value = ep.id;
                    option.text = ep.titulo;
                    capituloField.appendChild(option);
                });
            })
            .catch(error => console.error('Error al obtener los capítulos:', error));
    });
});