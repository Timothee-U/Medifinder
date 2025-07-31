document.getElementById('searchForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const lat = document.getElementById('lat').value;
  const lon = document.getElementById('lon').value;
  const category = document.getElementById('category').value;

  const res = await fetch('/search', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ lat, lon, category })
  });

  const data = await res.json();
  const places = data.features;
  const container = document.getElementById('results');
  container.innerHTML = places.map(place => `
    <div class="card">
      <h3>${place.properties.name || 'Unnamed'}</h3>
      <p>${place.properties.address_line1 || ''}</p>
      <p>${place.properties.address_line2 || ''}</p>
      <p>${place.properties.formatted || ''}</p>
    </div>
  `).join('');
});
