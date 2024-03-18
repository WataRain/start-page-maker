COLORS = ["Red", "Green", "Blue"]
NO_BGCOLOR = "#10198d"
NO_TEXTCOLOR = "#ffffff"
TITLE = "Start Page Maker by waflrain (2024)"
SUBTITLE = "Submitted as a final project in Harvard's CS50x 2024 course"
STYLE = """
html {
    align-items: center;
    color: $$ TEXT COLOR $$;
    text-shadow: 2px 2px 2px black;
    display: flex;
    font: 22px "Courier New", Courier, monospace;
    height: 100%;
    justify-content: center;
    margin: 0;
    background-color: $$ BACKGROUND COLOR $$;
    background-repeat: no-repeat;
    background-size: cover;
    background-position-x: center;
    background-position-y: center;
  }

  body {
    display: flex;
    margin: 1em;
    padding: 1em;
  }

  h1 {
    font-size: 2em;
    grid-column: 1 / -1;
    margin: 0;
    text-align: center;
  }
  
  p {
    font-size: 1em;
    grid-column: 1 / -1;
    margin: 0;
    text-align: center;
  }

  a {
    color: inherit;
    text-decoration: none;
  }

  a:focus,
  a:hover {
    color: #1d81b2;
  }

  nav {
    display: grid;
    row-gap: 2em;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    margin: 0 1em;
    min-width: 24em;
    padding: 1em 0;
  }

  ul {
    list-style-type: none;
    margin: 2em;
    padding: 0;
    white-space: nowrap;
  }

  img {
    border: 2px solid #313131;
    height: auto;
    object-fit: cover;
    object-position: 50% 100%;
    width: 8em;
  }
"""

HTML = f"""<!DOCTYPE html><html><head><title>Generated Start Page</title>
<style>{STYLE}</style></head><body><nav><h1>Start</h1>
<ul>$$ INSERT CONTENT HERE $$</ul>\n</nav>\n</body>\n</html>"""