<%inherit file="base.mako"/>

<div id="header-wrapper">
  <div id="header">
    <div class="location-block header-block">
      <h3>Location</h3>
      <div class="js-location">...</div>
    </div>
    <div class="score-block header-block">
      <h3>Score</h3>
      <div class="js-score">...</div>
    </div>
    <div class="moves-block header-block">
      <h3>Moves</h3>
      <div class="js-moves">...</div>
    </div>
  </div>
</div>
<div id="header-pad"></div>

<div id="gameplay">
  <div id="js-output"></div>
  <form id="move-form">
    &gt; <input id="move" name="move">
  </form>
</div>
