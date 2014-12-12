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
        {{!content}}
    </article>

      <footer>
        % if title != None:
            <p>Document source : <a href="/raw/{{file_name}}">{{file_name}}</a><br />
            Dernière mise à jour du document : <time datetime="{{mod_time}}">{{mod_time_f}} CEST</time>
        % end
        <p>Site fait main en Python véritable. <a href="/about">(+)</a></p>

      </footer>

    </body>
</html>
