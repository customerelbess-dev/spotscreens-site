(function () {
  'use strict';

  var year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  document.querySelectorAll('.slot img').forEach(function (img) {
    var label = img.parentElement.querySelector('.slot__file');
    function hideBroken() { img.style.display = 'none'; if (label) label.hidden = false; }
    function hideLabel() { if (label) label.hidden = true; }
    img.addEventListener('error', hideBroken);
    img.addEventListener('load', hideLabel);
    if (img.complete) {
      if (!img.naturalWidth) hideBroken();
      else hideLabel();
    }
  });

  document.querySelectorAll('.slot video').forEach(function (video) {
    var label = video.parentElement.querySelector('.slot__file');
    var starting = false;

    function hideBroken() { video.style.display = 'none'; if (label) label.hidden = false; }
    function hideLabel() { if (label) label.hidden = true; }
    video.addEventListener('error', hideBroken);
    video.addEventListener('playing', hideLabel);

    function arm() {
      video.removeAttribute('controls');
      video.controls = false;
      video.muted = true;
      video.defaultMuted = true;
      video.volume = 0;
      video.loop = true;
      video.autoplay = true;
      video.playsInline = true;
      video.setAttribute('muted', '');
      video.setAttribute('autoplay', '');
      video.setAttribute('loop', '');
      video.setAttribute('playsinline', 'true');
      video.setAttribute('webkit-playsinline', 'true');
      if ('disablePictureInPicture' in video) video.disablePictureInPicture = true;
      if ('disableRemotePlayback' in video) video.disableRemotePlayback = true;
    }

    function playLoop() {
      arm();
      if (starting || !video.paused) return;
      starting = true;
      var play = video.play();
      if (play && play.then) {
        play.then(function () { starting = false; hideLabel(); }).catch(function () { starting = false; });
      } else {
        starting = false;
      }
    }

    video.addEventListener('pause', function () {
      if (document.hidden) return;
      setTimeout(playLoop, 60);
    });
    video.addEventListener('ended', function () {
      try { video.currentTime = 0; } catch (e) {}
      playLoop();
    });
    video.addEventListener('loadeddata', playLoop);
    video.addEventListener('canplay', playLoop);

    document.addEventListener('visibilitychange', function () {
      if (!document.hidden) playLoop();
    });
    window.addEventListener('pageshow', playLoop);
    window.addEventListener('focus', playLoop);
    ['touchstart', 'touchend', 'pointerdown', 'click', 'scroll'].forEach(function (ev) {
      document.addEventListener(ev, playLoop, { passive: true });
    });

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) playLoop();
        });
      }, { threshold: 0.1 }).observe(video);
    }

    arm();
    playLoop();
  });

  var menuBtn = document.querySelector('[data-menu-btn]');
  var nav = document.querySelector('[data-nav]');

  function setMenu(open) {
    document.body.classList.toggle('is-menu-open', open);
    if (!menuBtn) return;
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    menuBtn.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
  }

  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      setMenu(!document.body.classList.contains('is-menu-open'));
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setMenu(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setMenu(false);
    });
    window.addEventListener('resize', function () {
      if (window.matchMedia('(min-width: 901px)').matches) setMenu(false);
    });
  }

  document.querySelectorAll('[data-tabs]').forEach(function (tabs) {
    var items = Array.prototype.slice.call(tabs.querySelectorAll('[data-tab]'));
    items.forEach(function (tab) {
      var btn = tab.querySelector('button');
      if (!btn) return;
      btn.addEventListener('click', function () {
        var open = tab.classList.contains('is-on');
        items.forEach(function (item) {
          var on = !open && item === tab;
          item.classList.toggle('is-on', on);
          var itemBtn = item.querySelector('button');
          if (itemBtn) itemBtn.setAttribute('aria-expanded', on ? 'true' : 'false');
        });
      });
    });
  });

  var root = document.querySelector('[data-slider]');
  if (!root) return;

  var track = root.querySelector('.slider__track');
  var slides = Array.prototype.slice.call(root.querySelectorAll('.slide'));
  var prev = root.querySelector('[data-prev]');
  var next = root.querySelector('[data-next]');
  var dotsWrap = root.querySelector('[data-dots]');
  var i = 0;
  var startX = 0;
  var dx = 0;
  var dragging = false;
  var timer;

  function go(n) {
    i = (n + slides.length) % slides.length;
    track.style.transform = 'translateX(' + (-i * 100) + '%)';
    if (dotsWrap) {
      dotsWrap.querySelectorAll('button').forEach(function (b, k) {
        b.classList.toggle('is-on', k === i);
      });
    }
  }

  function stop() { clearInterval(timer); }
  function start() {
    stop();
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    timer = setInterval(function () { go(i + 1); }, 4000);
  }

  function userGo(n) { go(n); start(); }

  if (dotsWrap) {
    slides.forEach(function (_, n) {
      var b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-label', 'Image ' + (n + 1));
      b.addEventListener('click', function () { userGo(n); });
      dotsWrap.appendChild(b);
    });
  }

  if (prev) prev.addEventListener('click', function () { userGo(i - 1); });
  if (next) next.addEventListener('click', function () { userGo(i + 1); });

  root.addEventListener('mouseenter', stop);
  root.addEventListener('mouseleave', start);

  root.addEventListener('touchstart', function (e) {
    startX = e.touches[0].clientX;
    dragging = true;
    dx = 0;
  }, { passive: true });
  root.addEventListener('touchmove', function (e) {
    if (!dragging) return;
    dx = e.touches[0].clientX - startX;
  }, { passive: true });
  root.addEventListener('touchend', function () {
    if (!dragging) return;
    dragging = false;
    if (dx > 50) userGo(i - 1);
    else if (dx < -50) userGo(i + 1);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') userGo(i - 1);
    if (e.key === 'ArrowRight') userGo(i + 1);
  });

  go(0);
  start();
})();
