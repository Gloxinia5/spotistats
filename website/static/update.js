setInterval(function(){ 
    getData();
}, 1000);
function getData(){
    fetch('/update')
    .then((res) => res.json())
    .then((data) => {
        try {
            document.getElementById('status').innerHTML = 'Currently Playing On Spotify'
            document.getElementById('rp-artist-name').innerHTML = data[0].item.artists[0].name;
            document.getElementById('rp-track-name').innerHTML = data[0].item.name;
            document.getElementById('rp-track-image').src = data[0].item.album.images[0].url;
            console.log('test2')
        }
        catch{
            document.getElementById('status').innerHTML = 'Recently Played'
            console.log('test1')
            document.getElementById('rp-artist-name').innerHTML = data[1].items[0].track.artists[0].name;
            document.getElementById('rp-track-name').innerHTML = data[1].items[0].track.name;
            document.getElementById('rp-track-image').src = data[1].items[0].track.album.images[0].url;
        }
        
    })
}