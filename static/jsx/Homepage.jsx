function SongList() {
    const songs = [];

    $.get('/songs', (res) => {

        for (const song of res) {
            songs.push(song);
        }
    }
    );

    return songs;

}


function HomePage() {
    const songs = SongList();
    console.log(songs);

    return (
        <div>
            <h1>MediocreBand</h1>
            <p>{songs}</p>
        </div>
    );
}

ReactDOM.render(<HomePage />, document.querySelector('#root'));