document.addEventListener('DOMContentLoaded', function() {
    setInterval(fetchData, 5000); // Atualiza a cada 5 segundos

    function fetchData() {
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.querySelector('#data-table tbody');
                tableBody.innerHTML = ''; // Limpa as linhas antigas
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.sensor_id}</td>
                        <td>${item.temperature}</td>
                        <td>${item.humidity}</td>
                    `;
                    tableBody.appendChild(row);
                });
            })
            .catch(error => console.error('Erro ao buscar dados:', error));
    }
});
