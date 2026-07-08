// Blog category filter — progressive enhancement.
// The CSS in blog.css uses the [data-cat] attribute on .blog__grid to
// hide/show cards whose data-cat attribute doesn't match. This script
// wires the filter buttons to that attribute. If JS fails, all posts show.
(function () {
  'use strict';
  var grid = document.querySelector('.blog__grid');
  var btns = document.querySelectorAll('.blog__filter-btn');
  if (!grid || !btns.length) return;

  function setCat(cat) {
    grid.setAttribute('data-cat', cat);
    for (var i = 0; i < btns.length; i++) {
      var b = btns[i];
      b.setAttribute('aria-pressed', b.dataset.cat === cat ? 'true' : 'false');
    }
  }

  for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function (e) {
      setCat(e.currentTarget.dataset.cat || 'all');
    });
  }
})();
