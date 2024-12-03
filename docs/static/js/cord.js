function toggleColorMode() {
    var element = document.documentElement;
    element.classList.toggle("dark-mode");

    const cordHandle = document.getElementById('cord-handle');

    if (element.classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'enabled');
        cordHandle.textContent = '☼'; 
    } else {
        localStorage.setItem('darkMode', 'disabled');
        cordHandle.textContent = '☾'; 
    }
}

document.addEventListener('DOMContentLoaded', () => {

    // ##### Cord JS #####

    const cordHandle = document.getElementById('cord-handle');
    const cordLine = document.getElementById('cord-line');
    
    if (document.documentElement.classList.contains('dark-mode')) {
        cordHandle.textContent = '☼';
    } else {
        cordHandle.textContent = '☾';
    }

    let isDragging = false;
    let startY = 0;
    let currentY = 0;
    const maxPullLength = 50; // Maximum pull length in pixels
    let isAnimating = false; // Add this flag to prevent multiple animations

    // Get initial positions
    const initialHandleTop = parseInt(window.getComputedStyle(cordHandle).top, 10);
    const initialLineHeight = parseInt(window.getComputedStyle(cordLine).height, 10);

    // Add click handler for animation
    cordHandle.addEventListener('click', (e) => {
        if (!isDragging && !isAnimating) {
            e.preventDefault();
            isAnimating = true;

            // Set up animation
            cordHandle.style.transition = 'top 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
            cordLine.style.transition = 'height 0.3s cubic-bezier(0.4, 0, 0.2, 1)';

            // Pull down
            cordHandle.style.top = `${initialHandleTop + maxPullLength}px`;
            cordLine.style.height = `${initialLineHeight + maxPullLength}px`;

            // After pulling down, spring back up
            setTimeout(() => {
                cordHandle.style.transition = 'top 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55)';
                cordLine.style.transition = 'height 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55)';
                
                cordHandle.style.top = `${initialHandleTop}px`;
                cordLine.style.height = `${initialLineHeight}px`;

                toggleColorMode();
                
                // Reset the animation flag after animation completes
                setTimeout(() => {
                    isAnimating = false;
                }, 500);
            }, 300);
        }
    });

    cordHandle.addEventListener('mousedown', (e) => {
        if (!isAnimating) {  // Only allow dragging if not animating
            e.preventDefault();
            isDragging = true;
            startY = e.clientY;

            cordHandle.style.transition = 'none';
            cordLine.style.transition = 'none';
        }
    });

    document.addEventListener('mousemove', (e) => {
        if (isDragging) {
            e.preventDefault(); // Prevents text selection while moving
            let dy = e.clientY - startY;
            if (dy > 0) {
                dy = Math.min(dy, maxPullLength);
                currentY = dy;
                // Update positions relative to initial positions
                cordHandle.style.top = `${initialHandleTop + dy}px`;
                cordLine.style.height = `${initialLineHeight + dy}px`;
            }
        }
    });

    document.addEventListener('mouseup', () => {
        if (isDragging) {
            isDragging = false;

            if (currentY > 45) {
                console.log('Cord pulled!');
                toggleColorMode();
            }

            // Enable transitions for springy effect upon release
            cordHandle.style.transition = 'top 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55)';
            cordLine.style.transition = 'height 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55)';

            // Reset the cord position with a springy animation
            cordHandle.style.top = `${initialHandleTop}px`;
            cordLine.style.height = `${initialLineHeight}px`;

            currentY = 0;
        }
    });
});
