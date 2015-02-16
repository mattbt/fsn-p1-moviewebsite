import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-image: url("bedge_grunge.png");
            font-family: 'Lato', sans-serif;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            
        }
        .movie_img{
            border: #fff solid 4px;
            border-radius: 10px;  
        }

        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        figcaption {
            position:absolute;
            top: 20px;
            left: 0px;
            width: 100%;   
        }
        .figcaptioncontent {
            width: 220px;
            height: 342px;
            margin: 0 auto;
            opacity:0;
            background-color: red;
            border: #fff solid 4px;
            border-radius: 10px;
            padding-top: 50px;

            /* Fallback for web browsers that don't support RGBa */
            background-color: rgb(0, 0, 0);
            /* RGBa with 0.6 opacity */
            background-color: rgba(0, 0, 0, 0.5);
            color: white;

            -webkit-font-smoothing: antialiased;
            -webkit-transition-delay: 0s;
            -webkit-transition-duration: 0.2s;
            -webkit-transition-property: all;
            -webkit-transition-timing-function: ease-in-out;
        }
        .figcaptioncontent:hover {
            opacity:1;
            visibility: show;
            cursor: pointer;
        }
        .storyline {
            padding: 0 15px 0 15px;
            text-align: justify;
        }
        .unique-nav-element {
            width:100%;
            height: 100%;
            text-align:center;
        }
        .unique-nav-element:hover i{
            color: red !important;
        }
        .navbar, .navbar-header {
            width: 100%;
        }
        .star{
            color: yellow
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.figcaptioncontent', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand unique-nav-element" href="#">My <i class="fa fa-heartbeat"></i> movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" >
    <figure>
        <img class="movie_img" src="{poster_image_url}" width="220" height="342" ></img>
        <figcaption>
            <div class="figcaptioncontent" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
                <span class="icon-star"></span> <h4 class="rating">IMDB  <i class="fa fa-star star"></i>  {movie_imdb_rating} / 10</h4> <p class="storyline">{movie_storyline}</p>  <span class="btn btn-success trailer_button">Watch Trailer</span>
            </div>
        </figcaption>
        
    </figure>
    <h3>{movie_title}</h3>
    <h5>{movie_year}</h5>
    
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline = movie.storyline,
            movie_year = movie.year,
            movie_imdb_rating = movie.imdbRating
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
