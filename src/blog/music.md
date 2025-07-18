# Music

---
Visible: True
Date: 2025-07-18
---

- Some days I listen to more music than I do silence. 
- I don't listen to lyrics.

---

<div id="music-container">
    <div id="song-list">
        <!-- Songs will be populated by JavaScript -->
    </div>
    <div id="description-panel">
        <div id="progress-indicator">1/85 songs</div>
        <div id="description-content">
            <p>Select a song to view its description</p>
        </div>
    </div>
</div>

<style>
#music-container {
    display: flex;
    gap: 4rem;
    height: 60vh;
    margin: 2rem 0;
    font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

#song-list {
    flex: 1;
    overflow: hidden;
    position: relative;
}

#description-panel {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

#description-content {
    text-align: center;
    color: var(--text-color, #100F0F);
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
}

#progress-indicator {
    font-size: 0.8rem;
    color: var(--text-muted, #666);
    margin-bottom: 1rem;
}

.song-item {
    padding: 0.5rem 0;
    cursor: pointer;
    transition: transform 0.5s ease;
}

.song-item:hover {
    transform: translateX(5px);
}



.song-name {
    color: var(--text-color, #100F0F);
    line-height: 1.4;
}

.artist {
    color: var(--text-muted, #666);
    font-size: 0.9em;
}

/* Mobile layout */
@media (max-width: 768px) {
    #music-container {
        flex-direction: column;
        height: 80vh;
    }
    
    #description-panel {
        order: -1;
        flex: 0 0 auto;
        margin-bottom: 1rem;
    }
    
    #song-list {
        flex: 1;
    }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
    :root {
        --text-color: #CECDC3;
        --text-muted: #999;
        --accent-color: #4385BE;
    }
}

/* Light mode (default) */
:root {
    --text-color: #100F0F;
    --text-muted: #666;
    --accent-color: #205EA6;
}
</style>

<script>
const songs = [
    // Transluce
    { period: "Transluce", title: "She only knows", artist: "starflyer 59", description: "" },
    { period: "Transluce", title: "jeans", artist: "2 hollis", description: "" },
    { period: "Transluce", title: "si tu m'aimes demain", artist: "lliona", description: "" },
    
    // Boston
    { period: "Boston", subPeriod: "May", title: "smithereens", artist: "boyish", description: "" },
    { period: "Boston", subPeriod: "May", title: "rap snitch knishes", artist: "mf doom", description: "" },
    { period: "Boston", subPeriod: "April", title: "Want to love - just raw", artist: "aloboi", description: "" },
    { period: "Boston", subPeriod: "April", title: "i come with mud", artist: "men i trust", description: "" },
    { period: "Boston", subPeriod: "April", title: "flesh without blood", artist: "grimes", description: "" },
    { period: "Boston", subPeriod: "April", title: "glistening", artist: "flipturn", description: "" },
    { period: "Boston", subPeriod: "April", title: "夏夜最後的浪漫", artist: "default", description: "" },
    
    // MATS
    { period: "MATS", subPeriod: "Feb, March", title: "bamboleo", artist: "gipsy kings", description: "" },
    { period: "MATS", subPeriod: "Feb, March", title: "B.O.R (birth of rap)", artist: "lil b", description: "" },
    { period: "MATS", subPeriod: "Feb, March", title: "space boy", artist: "Manny laurenko, LUCKI", description: "" },
    { period: "MATS", subPeriod: "Jan", title: "L$D", artist: "A$AP rocky", description: "" },
    { period: "MATS", subPeriod: "Jan", title: "velvet ring", artist: "big thief", description: "" },
    { period: "MATS", subPeriod: "Jan", title: "wild blue", artist: "john mayer", description: "" },
    { period: "MATS", subPeriod: "Jan", title: "?", artist: "vaundy", description: "" },
    
    // Sophomore Fall
    { period: "Sophomore Fall", title: "ma meillure ennemie", artist: "stromae, pomme, Arcane", description: "" },
    { period: "Sophomore Fall", title: "west savannah", artist: "isaiah rashad, SZA", description: "" },
    { period: "Sophomore Fall", title: "", artist: "laufey", description: "" },
    
    // Summer 2024
    { period: "Summer 2024", subPeriod: "July", title: "no one noticed", artist: "the marias", description: "" },
    { period: "Summer 2024", subPeriod: "July", title: "do ya think im sexy?", artist: "rod stewart", description: "" },
    { period: "Summer 2024", subPeriod: "July", title: "casual", artist: "chappel roan", description: "" },
    { period: "Summer 2024", subPeriod: "June", title: "unlock it", artist: "Abra, playboy carti, boys noize", description: "" },
    { period: "Summer 2024", subPeriod: "June", title: "marked till death", artist: "meat computer", description: "" },
    { period: "Summer 2024", subPeriod: "June", title: "i luv it", artist: "camila cabello, playboy carti", description: "" },
    { period: "Summer 2024", subPeriod: "May", title: "end of the beginning", artist: "djo", description: "" },
    { period: "Summer 2024", subPeriod: "May", title: "love lost", artist: "mac miller, the temper trap", description: "" },
    { period: "Summer 2024", subPeriod: "May", title: "A$AP forever (feat. moby)", artist: "A$AP Rocky, moby", description: "" },
    { period: "Summer 2024", subPeriod: "May", title: "everything is romantic", artist: "charlie xcx", description: "" },
    { period: "Summer 2024", subPeriod: "April", title: "vete", artist: "kevin kaarl", description: "" },
    { period: "Summer 2024", subPeriod: "April", title: "over the moon", artist: "the marias", description: "" },
    
    // Freshman Spring (London)
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "know my name", artist: "snow strippers", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "you and i", artist: "lucidbeatz, emilia ali", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "i like the way you kiss me", artist: "artemas", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "oblivion", artist: "grimes", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "kerosene", artist: "crystal castles", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "April", title: "intro", artist: "end of the world", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "Jan, Feb", title: "dolomeals", artist: "medhane", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "Jan, Feb", title: "johnny p's caddy", artist: "benny the butcher, J.cole", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "Jan, Feb", title: "daughters", artist: "john mayer", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "Jan, Feb", title: "sunrise", artist: "norah jones", description: "" },
    
    // Freshman Fall
    { period: "Freshman Fall", subPeriod: "December", title: "godlight", artist: "noah kahan", description: "" },
    { period: "Freshman Fall", subPeriod: "December", title: "from eden", artist: "hozier", description: "" },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "organon", artist: "men i trust", description: "" },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "lifelong song", artist: "men i trust", description: "" },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "can you hear the music", artist: "ludwig goransson", description: "" },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "paris, texas", artist: "lana del rey, SYML", description: "" },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "west coast", artist: "lana del rey", description: "" },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "say yes to heaven", artist: "lana del rey", description: "" },
    
    // Summer 2023
    { period: "Summer 2023", title: "manana", artist: "tainy, young miko, the marias", description: "" },
    { period: "Summer 2023", title: "tommy hanks", artist: "jakey", description: "" },
    
    // Senior Spring
    { period: "Senior Spring", subPeriod: "Part 2", title: "i wonder", artist: "kanye west", description: "" },
    { period: "Senior Spring", subPeriod: "Part 2", title: "nonviolent communication", artist: "metro boomin", description: "" },
    { period: "Senior Spring", subPeriod: "Part 2", title: "flashing lights", artist: "kanye", description: "" },
    { period: "Senior Spring", subPeriod: "Part 1", title: "you wouldn't know", artist: "zac crook", description: "" },
    
    // Senior Winter
    { period: "Senior Winter", title: "that nicotine", artist: "ava beathard", description: "" },
    { period: "Senior Winter", title: "superstar", artist: "boyish", description: "" },
    { period: "Senior Winter", title: "i got it", artist: "masho", description: "" },
    
    // Summer 2022
    { period: "Summer 2022", title: "uneasy", artist: "metronomy, spill tab", description: "" },
    { period: "Summer 2022", title: "temple of the dragon", artist: "adam brian paul", description: "" },
    
    // Junior Year
    { period: "Junior Year", title: "lovely day", artist: "bill withers", description: "" },
    { period: "Junior Year", title: "split", artist: "88rising, niki", description: "" },
    
    // Summer 2021 (Lifeguarding)
    { period: "Summer 2021 (Lifeguarding)", title: "beach bunny", artist: "cloud 9", description: "" },
    { period: "Summer 2021 (Lifeguarding)", title: "brazil", artist: "declan mckenna", description: "" },
    { period: "Summer 2021 (Lifeguarding)", title: "freaks", artist: "surf curse", description: "" },
    { period: "Summer 2021 (Lifeguarding)", title: "karma", artist: "sarah kinsley", description: "" },
    
    // Late COVID
    { period: "Late COVID", title: "hip", artist: "Mamamoo", description: "" },
    { period: "Late COVID", title: "bad girl", artist: "wooah", description: "" },
    
    // Freshman Year
    { period: "Freshman Year", title: "the louvre", artist: "lorde", description: "" },
    { period: "Freshman Year", title: "righteous", artist: "juice wrld", description: "" },
    { period: "Freshman Year", title: "ribs", artist: "lorde", description: "" },
    { period: "Freshman Year", title: "drunk", artist: "keshi", description: "" },
    { period: "Freshman Year", title: "skeletons", artist: "keshi", description: "" },
    { period: "Freshman Year", title: "lowkey", artist: "niki", description: "" }
];

let currentIndex = 0;
let songElements = [];
let scrollAccumulator = 0;
let scrollThreshold = 25;

function renderSongs() {
    const songList = document.getElementById('song-list');
    songList.innerHTML = '';
    songElements = [];
    
    updateVisibleSongs();
    
    // Select first song by default
    selectSong(0);
}

function updateVisibleSongs() {
    const songList = document.getElementById('song-list');
    const visibleCount = Math.min(15, songs.length);
    
    // Clear existing content
    songList.innerHTML = '';
    
    // Calculate the range of songs to display - selected song at top
    const startIndex = currentIndex;
    const endIndex = Math.min(startIndex + visibleCount, songs.length);
    
    // Add songs in the visible range
    for (let i = startIndex; i < endIndex; i++) {
        const song = songs[i];
        
        const songItem = document.createElement('div');
        songItem.className = 'song-item';
        songItem.setAttribute('data-index', i);
        
        if (i === currentIndex) {
            songItem.classList.add('selected');
        }
        
        const songName = document.createElement('div');
        songName.className = 'song-name';
        const prefix = (i === currentIndex) ? '> ' : '';
        songName.textContent = prefix + (song.title || '(untitled)');
        
        const artist = document.createElement('div');
        artist.className = 'artist';
        artist.textContent = `(${song.artist})`;
        
        songItem.appendChild(songName);
        songItem.appendChild(artist);
        
        songItem.addEventListener('click', () => {
            selectSong(i);
        });
        
        songList.appendChild(songItem);
    }
    
    // If we're near the end and don't have enough songs, add songs from the beginning
    if (endIndex - startIndex < visibleCount) {
        const remaining = visibleCount - (endIndex - startIndex);
        for (let i = 0; i < remaining && i < songs.length; i++) {
            const song = songs[i];
            
            const songItem = document.createElement('div');
            songItem.className = 'song-item';
            songItem.setAttribute('data-index', i);
            
            if (i === currentIndex) {
                songItem.classList.add('selected');
            }
            
            const songName = document.createElement('div');
            songName.className = 'song-name';
            const prefix = (i === currentIndex) ? '> ' : '';
            songName.textContent = prefix + (song.title || '(untitled)');
            
            const artist = document.createElement('div');
            artist.className = 'artist';
            artist.textContent = `(${song.artist})`;
            
            songItem.appendChild(songName);
            songItem.appendChild(artist);
            
            songItem.addEventListener('click', () => {
                selectSong(i);
            });
            
            songList.appendChild(songItem);
        }
    }
}

function selectSong(index) {
    currentIndex = index;
    
    // Update description
    updateDescription(songs[index]);
    
    // Re-render with selected song at top
    updateVisibleSongs();
}

function updateDescription(song) {
    const descriptionContent = document.getElementById('description-content');
    const progressIndicator = document.getElementById('progress-indicator');
    
    // Update progress
    progressIndicator.textContent = `${currentIndex + 1}/${songs.length} songs`;
    
    if (song.description) {
        descriptionContent.innerHTML = `<p>${song.description}</p>`;
    } else {
        descriptionContent.innerHTML = `<p style="font-style: italic; color: var(--text-muted);">No description available</p>`;
    }
}


function navigateUp() {
    if (currentIndex > 0) {
        selectSong(currentIndex - 1);
    } else {
        // Wrap to last song
        selectSong(songs.length - 1);
    }
}

function navigateDown() {
    if (currentIndex < songs.length - 1) {
        selectSong(currentIndex + 1);
    } else {
        // Wrap to first song
        selectSong(0);
    }
}

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    // Only handle arrow keys when the music container is in view
    const musicContainer = document.getElementById('music-container');
    const rect = musicContainer.getBoundingClientRect();
    const isInView = rect.top >= 0 && rect.bottom <= window.innerHeight;
    
    if (isInView || document.activeElement.closest('#music-container')) {
        if (e.key === 'ArrowUp') {
            e.preventDefault();
            navigateUp();
        } else if (e.key === 'ArrowDown') {
            e.preventDefault();
            navigateDown();
        }
    }
});

// Initialize when page loads
function initializeMusicPlayer() {
    renderSongs();
    
    // Mouse wheel/trackpad scroll navigation with accumulation
    document.getElementById('song-list').addEventListener('wheel', (e) => {
        e.preventDefault();
        
        scrollAccumulator += Math.abs(e.deltaY);
        
        if (scrollAccumulator >= scrollThreshold) {
            scrollAccumulator = 0;
            
            if (e.deltaY > 0) {
                // Scroll down - next song
                navigateDown();
            } else {
                // Scroll up - previous song
                navigateUp();
            }
        }
    });
}

// Initialize based on DOM state
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeMusicPlayer);
} else {
    initializeMusicPlayer();
}
</script>