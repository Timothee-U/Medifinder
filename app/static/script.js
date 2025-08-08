document.getElementById('searchForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const loading = document.getElementById('loading');
  const container = document.getElementById('results');

  // Show loading spinner and clear previous results/messages
  loading.hidden = false;
  container.innerHTML = '';

  const city = document.getElementById('city').value.trim();
  const category = document.getElementById('category').value;

  try {
    const res = await fetch('/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ city, category }),
    });

    const data = await res.json();

    if (!res.ok) {
      container.innerHTML = `<p>Error: ${data.error || 'Something went wrong'}</p>`;
      return;
    }

    const places = data.features || [];

    if (places.length === 0) {
      container.innerHTML = '<p>No results found for that city and category.</p>';
    } else {
      container.innerHTML = places
        .map(
          (place) => `
          <div class="card">
            <h3>${place.properties.name || 'Unnamed'}</h3>
            <p>${place.properties.address_line1 || ''}</p>
            <p>${place.properties.address_line2 || ''}</p>
            <p>${place.properties.formatted || ''}</p>
          </div>
        `
        )
        .join('');
    }
  } catch (error) {
    container.innerHTML = `<p>Error: ${error.message}</p>`;
  } finally {
    loading.hidden = true;
  }
});