function SongList() {
    let songs;
    $.get('/songs', (res) => {
        console.log(res);
        songs = res;
        console.log(songs);
    }
    );
    return songs;

}


function HomePage() {
    const songs = SongList();
    return (
        <div>
            <h1>MediocreBand</h1>
            <p>{songs}</p>
        </div>
    );
}

ReactDOM.render(<HomePage />, document.querySelector('#root'));