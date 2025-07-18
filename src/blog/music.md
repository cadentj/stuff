# Music

---
Visible: True
Date: 2025-07-18
---

<div id="music-container">
    <div id="song-list">
        <!-- Songs will be populated -->
    </div>
    <div id="description-panel">
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
    color: var(--text-muted, #666);
    flex: 1;
    display: flex;
    flex-direction: column;
    font-size: 0.8rem;
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
        height: 60vh    ;
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

/* Light mode colors */
#music-container {
    background-color: #FFFCF0;
    color: #100F0F;
}

.song-item.selected::before {
    color: #205EA6;
}

#description-content {
    color: #666;
}

.artist {
    color: #666;
}

.song-name {
    color: #100F0F;
}

/* Dark mode colors */
.dark-mode #music-container {
    background-color: #100F0F;
    color: #CECDC3;
}

.dark-mode .song-item.selected::before {
    color: #4385BE;
}

.dark-mode #description-content {
    color: #999;
}

.dark-mode .artist {
    color: #999;
}

.dark-mode .song-name {
    color: #CECDC3;
}
</style>

<script>
const songs = [
    // Summer 2025
    { period: "Summer 2025", title: "She only knows", artist: "starflyer 59", description: "" },
    { period: "Summer 2025", title: "jeans", artist: "2 hollis", description: "" },
    { period: "Summer 2025", title: "si tu m'aimes demain", artist: "lliona", description: "" },
    
    // Boston
    { period: "Boston", subPeriod: "May", title: "smithereens", artist: "boyish", description: "There was a week where this was literally the only song I listened to." },
    { period: "Boston", subPeriod: "May", title: "rap snitch knishes", artist: "mf doom", description: "" },
    { period: "Boston", subPeriod: "April", title: "i come with mud", artist: "men i trust", description: "" },
    { period: "Boston", subPeriod: "April", title: "flesh without blood", artist: "grimes", description: "" },
    { period: "Boston", subPeriod: "April", title: "glistening", artist: "flipturn", description: "" },
    { period: "Boston", subPeriod: "April", title: "夏夜最後的浪漫", artist: "default", description: "" },
    
    // MATS
    { period: "MATS", subPeriod: "Feb, March", title: "bamboleo", artist: "gipsy kings", description: "Not actually my most played gipsy kings song, but first one I saw on a Fire Force Tik Tok edit." },
    { period: "MATS", subPeriod: "Feb, March", title: "B.O.R (birth of rap)", artist: "lil b", description: "The first song on a Spotify daylist that I ended up saving in entirety." },
    { period: "MATS", subPeriod: "Feb, March", title: "space boy", artist: "Manny laurenko, LUCKI", description: "" },
    { period: "MATS", subPeriod: "Jan", title: "L$D", artist: "A$AP rocky", description: "" },
    { period: "MATS", subPeriod: "Jan", title: "velvet ring", artist: "big thief", description: "" },
    { period: "MATS", subPeriod: "Jan", title: "wild blue", artist: "john mayer", description: "Listening to this song brings back memories of the walk to Lighthaven -- at night, with Julian or Josh, or in the morning under the Berkeley sun." },
    { period: "MATS", subPeriod: "Jan", title: "踊り子", artist: "vaundy", description: "I think of Building C -- our little Neel scholar abode with its soft tofu lights and fuzzy carpet." },
    
    // Sophomore Fall
    { period: "Sophomore Fall", title: "ma meillure ennemie", artist: "stromae, pomme, Arcane", description: "I remember watching Arcane season 2 in Addison's apartment during Harvard/Yale with all my friends in town. Harris and Oliver were no life-ing poker, and Addison was trying to build hexbugs out of tooth brush heads." },
    { period: "Sophomore Fall", title: "west savannah", artist: "isaiah rashad, SZA", description: "" },
    { period: "Sophomore Fall", title: "", artist: "laufey", description: "Yay laufey!" },
    
    // Summer 2024
    { period: "Summer 2024", subPeriod: "July", title: "no one noticed", artist: "the marias", description: "" },
    { period: "Summer 2024", subPeriod: "July", title: "do ya think im sexy?", artist: "rod stewart", description: "Isabella introduced me to this song, her Dad loved it. She has a wonderful taste in music. Some blend of the Beatles and the worst bay area rap you've ever heard." },
    { period: "Summer 2024", subPeriod: "July", title: "casual", artist: "chappel roan", description: "" },
    { period: "Summer 2024", subPeriod: "June", title: "unlock it", artist: "Abra, playboy carti, boys noize", description: "I think of the walk from my apartment to 177 Huntington. The little park on the corner by Bluemoon Smoke Shop, filled with stinky summer geese." },
    { period: "Summer 2024", subPeriod: "June", title: "marked till death", artist: "meat computer", description: "There's a line in this song, 'you ever pooped your pants?' that Oliver found hilarious. He put it into a playlist when he was dating Skylar." },
    { period: "Summer 2024", subPeriod: "June", title: "i luv it", artist: "camila cabello, playboy carti", description: "" },
    { period: "Summer 2024", subPeriod: "May", title: "end of the beginning", artist: "djo", description: "" },
    { period: "Summer 2024", subPeriod: "May", title: "love lost", artist: "mac miller, the temper trap", description: "Blue bike rides across the bridge on Mass ave." },
    { period: "Summer 2024", subPeriod: "May", title: "A$AP forever (feat. moby)", artist: "A$AP Rocky, moby", description: "Isabella put me on A$AP." },
    { period: "Summer 2024", subPeriod: "May", title: "everything is romantic", artist: "charlie xcx", description: "" },
    { period: "Summer 2024", subPeriod: "April", title: "vete", artist: "kevin kaarl", description: "" },
    { period: "Summer 2024", subPeriod: "April", title: "over the moon", artist: "the marias", description: "" },
    
    // Freshman Spring (London)
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "know my name", artist: "snow strippers", description: "Blasting this in my suite, door open, working on some random paper with Josh Clymer. And also trying to solve intervening on intermediate states with NNsight. Avi loved Snow Strippers." },
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "you and i", artist: "lucidbeatz, emilia ali", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "i like the way you kiss me", artist: "artemas", description: "Song of the times. Ananya loved this one too." },
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "oblivion", artist: "grimes", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "March, April", title: "kerosene", artist: "crystal castles", description: "The gym on the first floor of Chapter Spitalfelds." },
    { period: "Freshman Spring (London)", subPeriod: "April", title: "intro", artist: "end of the world", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "Jan, Feb", title: "dolomeals", artist: "medhane", description: "The walk to St. Catherine's Docks, on the one or two days that semester where I actually went to school." },
    { period: "Freshman Spring (London)", subPeriod: "Jan, Feb", title: "johnny p's caddy", artist: "benny the butcher, J.cole", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "Jan, Feb", title: "daughters", artist: "john mayer", description: "" },
    { period: "Freshman Spring (London)", subPeriod: "Jan, Feb", title: "sunrise", artist: "norah jones", description: "" },
    
    // Freshman Fall
    { period: "Freshman Fall", subPeriod: "December", title: "godlight", artist: "noah kahan", description: "" },
    { period: "Freshman Fall", subPeriod: "December", title: "from eden", artist: "hozier", description: "" },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "organon", artist: "men i trust", description: "I played this in the Cass/Jiji/Paige's dorm sometimes, staring at the orange glow cast by the sunset lamp." },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "lifelong song", artist: "men i trust", description: "I remember the Fall rains in Boston, the nipping cold as it settled into Winter. I was alone a lot this semester -- this song reminds me of the tunnel connector by Curry." },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "can you hear the music", artist: "ludwig goransson", description: "" },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "paris, texas", artist: "lana del rey, SYML", description: "" },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "west coast", artist: "lana del rey", description: "I remember listening to this on a Southwest flight. It felt stale, weird, but I listened to it anyhow." },
    { period: "Freshman Fall", subPeriod: "Sept, Oct, Nov", title: "say yes to heaven", artist: "lana del rey", description: "" },
    
    // Summer 2023
    { period: "Summer 2023", title: "manana", artist: "tainy, young miko, the marias", description: "" },
    { period: "Summer 2023", title: "tommy hanks", artist: "jakey", description: "This was a weird period in my life. I wasn't very happy that summer." },
    
    // Senior Spring
    { period: "Senior Spring", subPeriod: "Part 2", title: "i wonder", artist: "kanye west", description: "I blasted kanye in the car a bunch second semester. Right around college app release date, I listened to a lot of Graduation in particular." },
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
    { period: "Junior Year", title: "lovely day", artist: "bill withers", description: "Mrs. Johnson-West played this song for our history class." },
    { period: "Junior Year", title: "split", artist: "88rising, niki", description: "" },
    
    // Summer 2021 (Lifeguarding)
    { period: "Summer 2021 (Lifeguarding)", title: "beach bunny", artist: "cloud 9", description: "The drive in my Subaru outback to the Bellaire Rec Center." },
    { period: "Summer 2021 (Lifeguarding)", title: "brazil", artist: "declan mckenna", description: "" },
    { period: "Summer 2021 (Lifeguarding)", title: "freaks", artist: "surf curse", description: "" },
    { period: "Summer 2021 (Lifeguarding)", title: "karma", artist: "sarah kinsley", description: "I swam a lot that summer with the Coogs -- we practiced in a weird, really sunny outdoor location." },
    
    // Late COVID
    { period: "Late COVID", title: "hip", artist: "Mamamoo", description: "" },
    { period: "Late COVID", title: "bad girl", artist: "wooah", description: "" },
    
    // Freshman Year
    { period: "Freshman Year", title: "the louvre", artist: "lorde", description: "" },
    { period: "Freshman Year", title: "righteous", artist: "juice wrld", description: "" },
    { period: "Freshman Year", title: "ribs", artist: "lorde", description: "This was Ananya's favorite Lorde song." },
    { period: "Freshman Year", title: "drunk", artist: "keshi", description: "" },
    { period: "Freshman Year", title: "skeletons", artist: "keshi", description: "" },
    { period: "Freshman Year", title: "lowkey", artist: "niki", description: "I was sad a lot during freshman/sophomore year." }
];

let currentIndex = 0;
let songElements = [];
let scrollAccumulator = 0;
let scrollThreshold = 25;
let touchScrollThreshold = 25;
let touchStartY = 0;

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
    const periodInfo = song.subPeriod ? `${song.period} - ${song.subPeriod}` : song.period;
    
    if (song.description) {
        descriptionContent.innerHTML = `
            <div style="margin-bottom: 1rem; font-size: 0.7rem; opacity: 0.7;">${currentIndex + 1}/${songs.length}</div>
            <div style="margin-bottom: 1rem;">${song.description}</div>
            <div style="font-style: italic;">${periodInfo}</div>
        `;
    } else {
        descriptionContent.innerHTML = `
            <div style="margin-bottom: 1rem; font-size: 0.7rem; opacity: 0.7;">${currentIndex + 1}/${songs.length}</div>
            <div style="margin-bottom: 1rem; font-style: italic;">No description available</div>
            <div style="font-style: italic;">${periodInfo}</div>
        `;
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
    
    // Mouse wheel/trackpad scroll navigation with accumulation (anywhere on screen)
    document.addEventListener('wheel', (e) => {
        // Only handle scroll if music container is visible
        const musicContainer = document.getElementById('music-container');
        const rect = musicContainer.getBoundingClientRect();
        const isInView = rect.top < window.innerHeight && rect.bottom > 0;
        
        if (!isInView) return;
        
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

    // Touch events for mobile
    document.addEventListener('touchstart', (e) => {
        const musicContainer = document.getElementById('music-container');
        const rect = musicContainer.getBoundingClientRect();
        const isInView = rect.top < window.innerHeight && rect.bottom > 0;
        
        if (isInView) {
            touchStartY = e.touches[0].clientY;
        }
    });

    document.addEventListener('touchmove', (e) => {
        const musicContainer = document.getElementById('music-container');
        const rect = musicContainer.getBoundingClientRect();
        const isInView = rect.top < window.innerHeight && rect.bottom > 0;
        
        if (!isInView) return;
        
        const touchY = e.touches[0].clientY;
        const deltaY = touchStartY - touchY;
        
        if (Math.abs(deltaY) > touchScrollThreshold) { // Threshold for touch swipe
            e.preventDefault();
            
            if (deltaY > 0) {
                // Swipe up - next song
                navigateDown();
            } else {
                // Swipe down - previous song
                navigateUp();
            }
            
            touchStartY = touchY; // Reset for continuous swiping
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