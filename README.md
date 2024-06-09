<h1>Hardcore Snake</h1>

<h2>Opis projektu</h2>
<p>Ten projekt to klasyczna gra w węża, nieco utrudniona napisana w Pythonie przy użyciu biblioteki Pygame. Gra polega na sterowaniu wężem, który porusza się po planszy, zjada jedzenie i unika przeszkód. Celem gry jest zdobycie jak najwyższego wyniku poprzez jedzenie, które powoduje wydłużanie węża.</p>

<h2>Instalacja</h2>
<p>Aby uruchomić tę grę, musisz mieć zainstalowany Python oraz bibliotekę Pygame. Możesz zainstalować Pygame za pomocą pip:</p>

<pre><code>pip install pygame</code></pre>

<h2>Uruchomienie gry</h2>
<p>Aby uruchomić grę, po prostu wykonaj skrypt Python:</p>

<pre><code>python main.py</code></pre>

<h2>Struktura projektu</h2>
<ul>
    <li><code>main.py</code>: Główny plik zawierający logikę gry i zarządzający grą.</li>
    <li><code>game_objects.py</code>: Plik zawierający logikę obiektów gry (wąż, jedzenie, przeszkody).</li>
    <li><code>assets/</code>: Katalog zawierający zasoby gry (obrazy, dźwięki).
        <ul>
            <li><code>images/</code>: Katalog zawierający obrazy.
                <ul>
                    <li><code>grass.jpg</code>: Tło gry.</li>
                    <li><code>head.png</code>: Obraz głowy węża.</li>
                    <li><code>body.png</code>: Obraz segmentu ciała węża.</li>
                    <li><code>food.png</code>: Obraz jedzenia.</li>
                    <li><code>stone.png</code>: Obraz przeszkody.</li>
                </ul>
            </li>
            <li><code>sounds/</code>: Katalog zawierający dźwięki.
                <ul>
                    <li><code>game-level-sound.wav</code>: Muzyka tła.</li>
                    <li><code>eat-sound.wav</code>: Dźwięk jedzenia.</li>
                    <li><code>cry-sound.wav</code>: Dźwięk kolizji.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><code>best_score.txt</code>: Plik przechowujący najlepszy wynik.</li>
</ul>

<h2>Ostrzegam gra jest bardzo uzależniająca, miłej zabawy!</h2>
