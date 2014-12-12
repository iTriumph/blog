<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="/static/style2.css" />
    <link rel="icon" href="/static/img/pypy_small128.png" />
    % if title == None:
        <title>Web log</title>
    % else:
        <title>{{title}}</title>
    % end
    </head>
    <body>
    <header>
        <h1>Web log</h1>
        <nav>
            <ul>
                <li><a href="/">&#x2302;</a></li>
                <li><a href="">&lt; /&gt;</a></li>
            </ul>
        </nav>
    </header>



    <article id="content">
        <h1>À propos</h1>
        <p>Moteur de site propulsé par :
            <ul>
                <li>Python {{py_ver}}</li>
                <li>Framework : <a href="http://bottlepy.org/">Bottle {{bottle_ver}}</a></li>
                <li>Rendu HTML : <a href="https://pypi.python.org/pypi/markdown2">Markdown2</a></li>
            </ul>
        </p>
        <p>
            Dernière mise à jour du moteur : {{last_update}}
        </p>
    </article>

      <footer>
        <p>Site fait main en Python véritable. <a href="/about">(+)</a><br /></p>

      </footer>
    </body>
</html>
