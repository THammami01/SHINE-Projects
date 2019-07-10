from bs4 import BeautifulSoup
import html5lib

html_doc = """









<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta name="defaultLanguage" content="en">
    <meta name="availableLanguages" content="en">

    

    <title>beautifulsoup4 · PyPI</title>
    <meta name="description" content="Screen-scraping library">

    <link rel="stylesheet" href="/static/css/warehouse.95256919.css">
    <link rel="stylesheet" href="/static/css/fontawesome.91df071f.css">
    <link rel="stylesheet" href="/static/css/regular.8819f1a9.css">
    <link rel="stylesheet" href="/static/css/solid.002489ee.css">
    <link rel="stylesheet" href="/static/css/brands.0c9eb08b.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400italic,600,600italic,700,700italic|Source+Code+Pro:500">
    <noscript>
      <link rel="stylesheet" href="/static/css/noscript.69d08c82.css">
    </noscript>

    

    <link rel="icon" href="/static/images/favicon.6a76275d.ico" type="image/x-icon">

    <link rel="alternate" type="application/rss+xml" title="RSS: 40 latest updates" href="/rss/updates.xml">
    <link rel="alternate" type="application/rss+xml" title="RSS: 40 newest packages" href="/rss/packages.xml">
    
    <link rel="canonical" href="https://pypi.org/project/beautifulsoup4/">
    

    <meta property="og:url" content="https://pypi.org/project/beautifulsoup4/">
    <meta property="og:site_name" content="PyPI">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://pypi.org/static/images/twitter.c0030826.jpg">
    <meta property="og:title" content="beautifulsoup4">
    <meta property="og:description" content="Screen-scraping library">

    <link rel="search" type="application/opensearchdescription+xml" title="PyPI" href="/opensearch.xml">

    
    <script
      src="https://cdn.ravenjs.com/3.26.2/raven.min.js"
      integrity="sha384-D6LXy67EIC102DTuqypxwQsTHgiatlbvg7q/1YAWFb6lRyZ1lIZ6bGDsX7jxHNKA"
      crossorigin="anonymous">
    </script>
    
    <script async
            data-ga-id="UA-55961911-1"
            data-sentry-frontend-dsn="https://3a67b35c9dc248a191d761410b095861@sentry.io/1231155"
            src="/static/js/warehouse.7c33004a.js">
    </script>
    
    
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-55961911-1"></script>
    <script defer src="https://www.fastly-insights.com/insights.js?k=6a52360a-f306-421e-8ed5-7417d0d4a4e9&dnt=true"></script>
  </head>

  <body data-controller="viewport-toggle">
    

    <!-- Accessibility: this link should always be the first piece of content inside the body-->
    <a href="#content" class="skip-to-content">Skip to main content</a>

    <button class="button button--primary button--switch-to-mobile hidden" data-target="viewport-toggle.switchToMobile" data-action="viewport-toggle#switchToMobile">
      Switch to mobile version
    </button>

    <section id="sticky-notifications" class="stick-to-top js-stick-to-top">
      <!-- Add browser warning. Will show for ie9 and below -->
      <!--[if IE]>
      <div class="notification-bar notification-bar--warning" role="status">
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning:</span>
        </span>
        <span class="notification-bar__message">You are using an unsupported browser, upgrade to a newer version.</span>
      </div>
      <![endif]-->
      
      <noscript>
      <div class="notification-bar notification-bar--warning" role="status">
        
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning:</span>
        </span>
        <span class="notification-bar__message">Some features may not work without JavaScript. Please try enabling it if you encounter problems.</span>
      </div>
      </noscript>
    </section>

    
      <div data-html-include="/_includes/flash-messages/">
      </div>
    

    

    
      <div data-html-include="/_includes/session-notifications/">
      </div>
    

    <header class="site-header ">
      <div class="site-container">
        <div class="split-layout">
          
          <div class="split-layout">
            <div>
              <a class="site-header__logo" href="/">
                <img alt="PyPI" src="/static/images/logo-small.6eef541e.svg">
              </a>
            </div>

            <form class="search-form search-form--primary" action="/search/" role="search">
              <label for="search" class="sr-only">Search PyPI</label>
              <input id="search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="">
              
              <button type="submit" class="search-form__button">
                <i class="fa fa-search" aria-hidden="true"></i>
                <span class="sr-only">Search</span>
              </button>
            </form>
          </div>
          

          <div data-html-include="/_includes/current-user-indicator/">
            <nav id="user-indicator" class="horizontal-menu horizontal-menu--light horizontal-menu--tall" aria-label="Main navigation">
  <a class="horizontal-menu__link horizontal-menu__link--remove-on-mobile" href="/help/">Help</a>
  <a class="horizontal-menu__link horizontal-menu__link--remove-on-mobile" href="https://donate.pypi.org">Donate</a>
  <a class="horizontal-menu__link" href="/account/login/">Log in</a>
  <a class="horizontal-menu__link" href="/account/register/">Register</a>
</nav>
          </div>
        </div>
      </div>
    </header>

    
    <section class="mobile-search">
      <form class="search-form search-form--fullwidth" action="/search/" role="search">
        <label for="mobile-search" class="sr-only">Search PyPI</label>
        <input id="mobile-search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="">
        
        <button type="submit" class="search-form__button">
          <i class="fa fa-search" aria-hidden="true"></i>
          <span class="sr-only">Search</span>
        </button>
      </form>
    </section>
    

    <main id="content">
      
<section class="banner">
  <div class="package-header">
    <div class="package-header__left">
      <h1 class="package-header__name">
        beautifulsoup4 4.7.1
      </h1>

      
      <p class="package-header__pip-instructions">
        <span id="pip-command">pip install beautifulsoup4</span>
        <button class="-js-copy-pip-command tooltipped tooltipped-s" data-clipboard-target="#pip-command" aria-label="Copy to clipboard" data-original-label="Copy to clipboard">
          <i class="fa fa-copy" aria-hidden="true"></i>
          <span class="sr-only">Copy PIP instructions<span>
        </button>
      </p>
      
    </div>

    <div class="package-header__right">
      
      <a class="status-badge status-badge--good" href="/project/beautifulsoup4/">Latest version</a>
      
      <p class="package-header__date">Last released: <time class="-js-relative-time" datetime="2019-01-07T00:53:18+0000" data-controller="localized-time" data-localized-time-relative="true">
  Jan 7, 2019
</time></p>
    </div>
  </div>
</section>

<section class="horizontal-section horizontal-section--grey horizontal-section--thin">
  <div class="site-container">
    <div class="split-layout split-layout--middle package-description">
    
      <p class="package-description__summary">Screen-scraping library</p>
    
    <div data-html-include="/_includes/edit-project-button/beautifulsoup4">
    </div>
    </div>
  </div>
</section>

<section data-controller="project-tabs">
  <div class="tabs-container">
    <div class="vertical-tabs">
      <div class="vertical-tabs__tabs">
        <div class="sidebar-section">
          <h3 class="sidebar-section__title">Navigation</h3>
            <nav role="tablist">
              <a id="description-tab" data-target="project-tabs.tab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--is-active" href="#description" role="tab">
                <i class="fa fa-align-left" aria-hidden="true"></i>
                Project description
              </a>
              <a id="history-tab" data-target="project-tabs.tab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon" href="#history" role="tab">
                <i class="fa fa-history" aria-hidden="true"></i>
                Release history
              </a>
              
                <a id="files-tab" data-target="project-tabs.tab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon" href="#files" role="tab">
                  <i class="fa fa-download" aria-hidden="true"></i>
                  Download files
                </a>
              
            </nav>
        </div>
        
<div class="sidebar-section">
  <h3 class="sidebar-section__title">Project links</h3>
  
  
  <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" href="http://www.crummy.com/software/BeautifulSoup/bs4/" rel="nofollow">
    


  


<i class="fas fa-home" aria-hidden="true"></i>Homepage
  </a>
  
  
  
  <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" href="http://www.crummy.com/software/BeautifulSoup/bs4/download/" rel="nofollow">
    


   


<i class="fas fa-cloud-download-alt" aria-hidden="true"></i>Download
  </a>
  
  
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Statistics</h3>
  
  <p>View statistics for this project via <a
          href="https://libraries.io/pypi/beautifulsoup4" title="External link" target="_blank" rel="noopener">Libraries.io</a>, or by using
    <a href="https://packaging.python.org/guides/analyzing-pypi-package-downloads/" target="_blank" rel="noopener">Google
      BigQuery</a></p>
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Meta</h3>
  
  <p><strong>License:</strong> MIT License (MIT)</p>
  
  
    <p><strong>Author:</strong> <a href="mailto:leonardr@segfault.org">Leonard Richardson</a></p>
  
  
  
  
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Maintainers</h3>
  
    
    <span class="sidebar-section__maintainer">
      <a href="/user/leonard/" aria-label="leonard" class="sidebar-section__user-gravatar">
        <img src="https://warehouse-camo.cmh1.psfhosted.org/c5caa34d0062a04d6d09cab71355954f188822a3/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f62383361616135653563383132393938376338633534663239373465383464333f73697a653d3530" height="50" width="50" alt="Avatar for leonard from gravatar.com" title="Avatar for leonard from gravatar.com">
      </a>
      <a href="/user/leonard/" class="sidebar-section__user-gravatar-text">
        leonard
      </a>
    </span>
  
</div>


<div class="sidebar-section classifiers">
  <h3>Classifiers</h3>
  <dl>
    
    <dt>Development Status</dt>
    
    <dd>
    <a href="/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable">
      5 - Production/Stable
    </a>
    </dd>
    
    
    <dt>Intended Audience</dt>
    
    <dd>
    <a href="/search/?c=Intended+Audience+%3A%3A+Developers">
      Developers
    </a>
    </dd>
    
    
    <dt>License</dt>
    
    <dd>
    <a href="/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License">
      OSI Approved :: MIT License
    </a>
    </dd>
    
    
    <dt>Programming Language</dt>
    
    <dd>
    <a href="/search/?c=Programming+Language+%3A%3A+Python">
      Python
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+2.7">
      Python :: 2.7
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3">
      Python :: 3
    </a>
    </dd>
    
    
    <dt>Topic</dt>
    
    <dd>
    <a href="/search/?c=Topic+%3A%3A+Software+Development+%3A%3A+Libraries+%3A%3A+Python+Modules">
      Software Development :: Libraries :: Python Modules
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Topic+%3A%3A+Text+Processing+%3A%3A+Markup+%3A%3A+HTML">
      Text Processing :: Markup :: HTML
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Topic+%3A%3A+Text+Processing+%3A%3A+Markup+%3A%3A+SGML">
      Text Processing :: Markup :: SGML
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Topic+%3A%3A+Text+Processing+%3A%3A+Markup+%3A%3A+XML">
      Text Processing :: Markup :: XML
    </a>
    </dd>
    
    
  </dl>
</div>


      </div>
      <div class="vertical-tabs__panel">
        <!-- mobile menu -->
        <nav>
          <a id="mobile-description-tab" data-target="project-tabs.mobileTab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--mobile vertical-tabs__tab--no-top-border vertical-tabs__tab--is-active" href="#description">
            <i class="fa fa-align-left" aria-hidden="true"></i>
            Project description
          </a>
          <a id="mobile-data-tab" data-target="project-tabs.mobileTab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--mobile" href="#data">
            <i class="fa fa-info-circle" aria-hidden="true"></i>
            Project details
          </a>
          <a id="mobile-history-tab" data-target="project-tabs.mobileTab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--mobile" href="#history">
            <i class="fa fa-history" aria-hidden="true"></i>
            Release history
          </a>
          
          <a id="mobile-files-tab" data-target="project-tabs.mobileTab" data-action="project-tabs#onTabClick" class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--mobile" href="#files">
            <i class="fa fa-download" aria-hidden="true"></i>
            Download files
          </a>
          
        </nav>

        
        <div id="description" data-target="project-tabs.content" class="vertical-tabs__content" role="tabpanel" aria-labelledby="description-tab mobile-description-tab">
          <h2 class="page-title">Project description</h2>
          
          <div class="project-description">
            <p>Beautiful Soup is a library that makes it easy to scrape information
from web pages. It sits atop an HTML or XML parser, providing Pythonic
idioms for iterating, searching, and modifying the parse tree.</p>
<h1>Quick start</h1>
<pre><code>  &gt;&gt;&gt; from bs4 import BeautifulSoup
  &gt;&gt;&gt; soup = BeautifulSoup("&lt;p&gt;Some&lt;b&gt;bad&lt;i&gt;HTML")
  &gt;&gt;&gt; print soup.prettify()
  &lt;html&gt;
   &lt;body&gt;
    &lt;p&gt;
     Some
     &lt;b&gt;
      bad
      &lt;i&gt;
       HTML
      &lt;/i&gt;
     &lt;/b&gt;
    &lt;/p&gt;
   &lt;/body&gt;
  &lt;/html&gt;
  &gt;&gt;&gt; soup.find(text="bad")
  u'bad'

  &gt;&gt;&gt; soup.i
  &lt;i&gt;HTML&lt;/i&gt;

  &gt;&gt;&gt; soup = BeautifulSoup("&lt;tag1&gt;Some&lt;tag2/&gt;bad&lt;tag3&gt;XML", "xml")
  &gt;&gt;&gt; print soup.prettify()
  &lt;?xml version="1.0" encoding="utf-8"&gt;
  &lt;tag1&gt;
   Some
   &lt;tag2 /&gt;
   bad
   &lt;tag3&gt;
    XML
   &lt;/tag3&gt;
  &lt;/tag1&gt;
</code></pre>
<p>To go beyond the basics, <a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/" rel=nofollow>comprehensive documentation is available</a>.</p>
<h1>Links</h1>
<ul>
<li><a href="http://www.crummy.com/software/BeautifulSoup/bs4/" rel=nofollow>Homepage</a></li>
<li><a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/" rel=nofollow>Documentation</a></li>
<li><a href="http://groups.google.com/group/beautifulsoup/" rel=nofollow>Discussion group</a></li>
<li><a href="https://code.launchpad.net/beautifulsoup/" rel=nofollow>Development</a></li>
<li><a href="https://bugs.launchpad.net/beautifulsoup/" rel=nofollow>Bug tracker</a></li>
<li><a href="https://bazaar.launchpad.net/%7Eleonardr/beautifulsoup/bs4/view/head:/CHANGELOG" rel=nofollow>Complete changelog</a></li>
</ul>
<h1>Building the documentation</h1>
<p>The bs4/doc/ directory contains full documentation in Sphinx
format. Run <code>make html</code> in that directory to create HTML
documentation.</p>
<h1>Running the unit tests</h1>
<p>Beautiful Soup supports unit test discovery from the project root directory:</p>
<pre><code> $ nosetests
</code></pre>
<pre><code> $ python -m unittest discover -s bs4 # Python 2.7 and up
</code></pre>
<p>If you checked out the source tree, you should see a script in the
home directory called test-all-versions. This script will run the unit
tests under Python 2.7, then create a temporary Python 3 conversion of
the source and run the unit tests again under Python 3.</p>

          </div>
          
        </div>

        
        <div id="data" data-target="project-tabs.content" class="vertical-tabs__content" role="tabpanel" aria-labelledby="mobile-data-tab">
          <h2 class="page-title">Project details</h2>
          
<div class="sidebar-section">
  <h3 class="sidebar-section__title">Project links</h3>
  
  
  <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" href="http://www.crummy.com/software/BeautifulSoup/bs4/" rel="nofollow">
    


  


<i class="fas fa-home" aria-hidden="true"></i>Homepage
  </a>
  
  
  
  <a class="vertical-tabs__tab vertical-tabs__tab--with-icon vertical-tabs__tab--condensed" href="http://www.crummy.com/software/BeautifulSoup/bs4/download/" rel="nofollow">
    


   


<i class="fas fa-cloud-download-alt" aria-hidden="true"></i>Download
  </a>
  
  
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Statistics</h3>
  
  <p>View statistics for this project via <a
          href="https://libraries.io/pypi/beautifulsoup4" title="External link" target="_blank" rel="noopener">Libraries.io</a>, or by using
    <a href="https://packaging.python.org/guides/analyzing-pypi-package-downloads/" target="_blank" rel="noopener">Google
      BigQuery</a></p>
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Meta</h3>
  
  <p><strong>License:</strong> MIT License (MIT)</p>
  
  
    <p><strong>Author:</strong> <a href="mailto:leonardr@segfault.org">Leonard Richardson</a></p>
  
  
  
  
</div>


<div class="sidebar-section">
  <h3 class="sidebar-section__title">Maintainers</h3>
  
    
    <span class="sidebar-section__maintainer">
      <a href="/user/leonard/" aria-label="leonard" class="sidebar-section__user-gravatar">
        <img src="https://warehouse-camo.cmh1.psfhosted.org/c5caa34d0062a04d6d09cab71355954f188822a3/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f62383361616135653563383132393938376338633534663239373465383464333f73697a653d3530" height="50" width="50" alt="Avatar for leonard from gravatar.com" title="Avatar for leonard from gravatar.com">
      </a>
      <a href="/user/leonard/" class="sidebar-section__user-gravatar-text">
        leonard
      </a>
    </span>
  
</div>


<div class="sidebar-section classifiers">
  <h3>Classifiers</h3>
  <dl>
    
    <dt>Development Status</dt>
    
    <dd>
    <a href="/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable">
      5 - Production/Stable
    </a>
    </dd>
    
    
    <dt>Intended Audience</dt>
    
    <dd>
    <a href="/search/?c=Intended+Audience+%3A%3A+Developers">
      Developers
    </a>
    </dd>
    
    
    <dt>License</dt>
    
    <dd>
    <a href="/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License">
      OSI Approved :: MIT License
    </a>
    </dd>
    
    
    <dt>Programming Language</dt>
    
    <dd>
    <a href="/search/?c=Programming+Language+%3A%3A+Python">
      Python
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+2.7">
      Python :: 2.7
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3">
      Python :: 3
    </a>
    </dd>
    
    
    <dt>Topic</dt>
    
    <dd>
    <a href="/search/?c=Topic+%3A%3A+Software+Development+%3A%3A+Libraries+%3A%3A+Python+Modules">
      Software Development :: Libraries :: Python Modules
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Topic+%3A%3A+Text+Processing+%3A%3A+Markup+%3A%3A+HTML">
      Text Processing :: Markup :: HTML
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Topic+%3A%3A+Text+Processing+%3A%3A+Markup+%3A%3A+SGML">
      Text Processing :: Markup :: SGML
    </a>
    </dd>
    
    <dd>
    <a href="/search/?c=Topic+%3A%3A+Text+Processing+%3A%3A+Markup+%3A%3A+XML">
      Text Processing :: Markup :: XML
    </a>
    </dd>
    
    
  </dl>
</div>

          <br>
        </div>

        
        <div id="history" data-target="project-tabs.content" class="vertical-tabs__content" role="tabpanel" aria-labelledby="history-tab mobile-history-tab">
          <h2 class="page-title split-layout">
            <span>Release history</span>
            <a class="reset-text margin-top" href="/help/#project-release-notifications">Release notifications</a>
          </h2>

          <section class="release-timeline">
            
            
            
            
            <div class="release release--latest release--current">
              <div class="release__meta">
                
                <span class="badge">This version</span>
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/blue-cube.e6165d35.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.7.1/">
                <p class="release__version">
                  4.7.1 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2019-01-07T00:53:18+0000" data-controller="localized-time">
  Jan 7, 2019
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.7.0/">
                <p class="release__version">
                  4.7.0 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2018-12-31T17:51:20+0000" data-controller="localized-time">
  Dec 31, 2018
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.6.3/">
                <p class="release__version">
                  4.6.3 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2018-08-12T16:39:46+0000" data-controller="localized-time">
  Aug 12, 2018
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.6.2/">
                <p class="release__version">
                  4.6.2 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2018-08-12T15:04:59+0000" data-controller="localized-time">
  Aug 12, 2018
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.6.1/">
                <p class="release__version">
                  4.6.1 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2018-07-28T23:39:05+0000" data-controller="localized-time">
  Jul 28, 2018
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.6.0/">
                <p class="release__version">
                  4.6.0 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2017-05-07T13:52:31+0000" data-controller="localized-time">
  May 7, 2017
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.5.3/">
                <p class="release__version">
                  4.5.3 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2017-01-02T15:08:00+0000" data-controller="localized-time">
  Jan 2, 2017
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.5.2/">
                <p class="release__version">
                  4.5.2 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2017-01-02T14:55:08+0000" data-controller="localized-time">
  Jan 2, 2017
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.5.1/">
                <p class="release__version">
                  4.5.1 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2016-08-03T02:43:11+0000" data-controller="localized-time">
  Aug 3, 2016
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.5.0/">
                <p class="release__version">
                  4.5.0 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2016-07-20T10:37:57+0000" data-controller="localized-time">
  Jul 20, 2016
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.4.1/">
                <p class="release__version">
                  4.4.1 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2015-09-29T00:19:38+0000" data-controller="localized-time">
  Sep 29, 2015
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.4.0/">
                <p class="release__version">
                  4.4.0 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2015-07-03T15:22:53+0000" data-controller="localized-time">
  Jul 3, 2015
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.3.2/">
                <p class="release__version">
                  4.3.2 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2013-10-02T12:37:31+0000" data-controller="localized-time">
  Oct 2, 2013
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.3.1/">
                <p class="release__version">
                  4.3.1 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:47+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.3.0/">
                <p class="release__version">
                  4.3.0 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:43+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.2.1/">
                <p class="release__version">
                  4.2.1 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:40+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.2.0/">
                <p class="release__version">
                  4.2.0 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:37+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.1.3/">
                <p class="release__version">
                  4.1.3 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:34+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.1.2/">
                <p class="release__version">
                  4.1.2 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:30+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.1.1/">
                <p class="release__version">
                  4.1.1 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:27+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.1.0/">
                <p class="release__version">
                  4.1.0 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:24+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.0.5/">
                <p class="release__version">
                  4.0.5 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:20+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.0.4/">
                <p class="release__version">
                  4.0.4 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:15+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.0.3/">
                <p class="release__version">
                  4.0.3 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:12+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.0.2/">
                <p class="release__version">
                  4.0.2 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:07+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
            
            <div class="release release--oldest">
              <div class="release__meta">
                
              </div>

              <div class="release__graphic">
                
                <div class="release__line"></div>
                
                
                <img class="release__node" alt="History Node" src="https://pypi.org/static/images/white-cube.8c3a6fe9.svg">
                
              </div>

              <a class="card release__card" href="/project/beautifulsoup4/4.0.1/">
                <p class="release__version">
                  4.0.1 
                </p>
                <p class="release__version-date">
                  <time class="tooltipped tooltipped-s -js-relative-time" datetime="2014-01-21T05:35:03+0000" data-controller="localized-time">
  Jan 21, 2014
</time>
                </p>
              </a>
            </div>
            
          </section>
        </div>

        
          
          <div id="files" data-target="project-tabs.content" class="vertical-tabs__content" role="tabpanel" aria-labelledby="files-tab mobile-files-tab">
            <h2 class="page-title">Download files</h2>
            <p>Download the file for your platform. If you're not sure which to choose, learn more about <a href="https://packaging.python.org/installing/" title="External link" target="_blank" rel="noopener">installing packages</a>.</p>

            <table class="table table--downloads">
              <thead>
                <tr>
                  <th class="table__filename">
                    Filename, size &amp; hash
                    <a href="https://pip.pypa.io/en/stable/reference/pip_install/#hash-checking-mode" target="_blank" rel="noopener" class="tooltipped tooltipped-n" aria-label="what's this?" data-original-label="what's this?">
                      <i class="fa fa-question-circle" aria-hidden="true"></i>
                      <span class="sr-only">SHA256 hash help</span>
                    </a>
                  </th>
                  <th class="table__type">File type</th>
                  <th class="table__version">Python version</th>
                  <th class="table__upload-date">Upload date</th>
                </tr>
              </thead>
              <tbody>
                
                <tr>
                  <td>
                    <a href="https://files.pythonhosted.org/packages/8b/0e/048a2f88bc4be5e3697df9dc1f7b9d5c9c75be62676feeeb91d2e896c5ea/beautifulsoup4-4.7.1-py2-none-any.whl">
                      beautifulsoup4-4.7.1-py2-none-any.whl
                    </a>
                     (94.4 kB)
                    <a class="-js-copy-hash table__sha256-link tooltipped tooltipped-s" aria-label="Copy to clipboard" data-original-label="Copy to clipboard" data-clipboard-text="ba6d5c59906a85ac23dadfe5c88deaf3e179ef565f4898671253e50a78680718">
                      <i class="fa fa-copy" aria-hidden="true"></i>
                      <span class="sr-only">Copy SHA256 hash</span>
                      SHA256
                    </a>
                  </td>
                  <td>
                    Wheel
                  </td>
                  <td>
                    
                      py2
                    
                  </td>
                  <td><time class="tooltipped tooltipped-s -js-relative-time" datetime="2019-01-07T00:53:18+0000" data-controller="localized-time">
  Jan 7, 2019
</time></td>
                </tr>
                
                <tr>
                  <td>
                    <a href="https://files.pythonhosted.org/packages/1d/5d/3260694a59df0ec52f8b4883f5d23b130bc237602a1411fa670eae12351e/beautifulsoup4-4.7.1-py3-none-any.whl">
                      beautifulsoup4-4.7.1-py3-none-any.whl
                    </a>
                     (94.3 kB)
                    <a class="-js-copy-hash table__sha256-link tooltipped tooltipped-s" aria-label="Copy to clipboard" data-original-label="Copy to clipboard" data-clipboard-text="034740f6cb549b4e932ae1ab975581e6103ac8f942200a0e9759065984391858">
                      <i class="fa fa-copy" aria-hidden="true"></i>
                      <span class="sr-only">Copy SHA256 hash</span>
                      SHA256
                    </a>
                  </td>
                  <td>
                    Wheel
                  </td>
                  <td>
                    
                      py3
                    
                  </td>
                  <td><time class="tooltipped tooltipped-s -js-relative-time" datetime="2019-01-07T00:53:20+0000" data-controller="localized-time">
  Jan 7, 2019
</time></td>
                </tr>
                
                <tr>
                  <td>
                    <a href="https://files.pythonhosted.org/packages/80/f2/f6aca7f1b209bb9a7ef069d68813b091c8c3620642b568dac4eb0e507748/beautifulsoup4-4.7.1.tar.gz">
                      beautifulsoup4-4.7.1.tar.gz
                    </a>
                     (167.1 kB)
                    <a class="-js-copy-hash table__sha256-link tooltipped tooltipped-s" aria-label="Copy to clipboard" data-original-label="Copy to clipboard" data-clipboard-text="945065979fb8529dd2f37dbb58f00b661bdbcbebf954f93b32fdf5263ef35348">
                      <i class="fa fa-copy" aria-hidden="true"></i>
                      <span class="sr-only">Copy SHA256 hash</span>
                      SHA256
                    </a>
                  </td>
                  <td>
                    Source
                  </td>
                  <td>
                    
                      None
                    
                  </td>
                  <td><time class="tooltipped tooltipped-s -js-relative-time" datetime="2019-01-07T00:53:22+0000" data-controller="localized-time">
  Jan 7, 2019
</time></td>
                </tr>
                
              </tbody>
            </table>
          </div>
        
      </div>
    </div>
  </div>
</section>

    </main>

    <footer class="footer" role="contentinfo">
      <div class="footer__logo">
        <img src="/static/images/white-cube.8c3a6fe9.svg" alt="Logo" class="-js-white-cube">
      </div>

      <div class="footer__menus">
        <ul class="footer__menu">
          <li>
            <h2>Help</h2>
          </li>
          <li><a href="https://packaging.python.org/installing/" title="External link" target="_blank" rel="noopener">Installing packages</a></li>
          <li><a href="https://packaging.python.org/tutorials/packaging-projects/" title="External link" target="_blank" rel="noopener">Uploading packages</a></li>
          <li><a href="https://packaging.python.org/" title="External link" target="_blank" rel="noopener">User guide</a></li>
          <li><a href="/help/">FAQs</a></li>
        </ul>
        <ul class="footer__menu">
          <li>
            <h2>About PyPI</h2>
          </li>
          <li><a href="https://twitter.com/PyPI" title="External link" target="_blank" rel="noopener">PyPI on Twitter</a></li>
          <li><a href="https://dtdg.co/pypi" title="External link" target="_blank" rel="noopener">Infrastructure dashboard</a></li>
          <li><a href="https://www.python.org/dev/peps/pep-0541/" title="External link" target="_blank" rel="noopener">Package index name retention</a></li>
          <li><a href="/sponsors/">Our sponsors</a></li>
        </ul>


        <ul class="footer__menu">
          <li>
            <h2>Contributing to PyPI</h2>
          </li>
          <li><a href="/help/#feedback">Bugs and feedback</a></li>
          <li><a href="https://github.com/pypa/warehouse" title="External link" target="_blank" rel="noopener">Contribute on GitHub</a></li>
          <li><a href="https://github.com/pypa/warehouse/graphs/contributors" title="External link" target="_blank" rel="noopener">Development credits</a></li>
        </ul>
        <ul class="footer__menu">
          <li>
            <h2>Using PyPI</h2>
          </li>
          <li><a href="https://www.pypa.io/en/latest/code-of-conduct/" title="External link" target="_blank" rel="noopener">Code of conduct</a></li>
          <li><a href="/security/">Report security issue</a></li>
          <li><a href="https://www.python.org/privacy/" title="External link" target="_blank" rel="noopener">Privacy policy</a></li>
          <li><a href="/policy/terms-of-use/">Terms of use</a></li>
        </ul>
      </div>

      <hr class="footer__divider">

      <div class="footer__text">
        
        <p>Status: <a href="https://status.python.org/" title="External link" target="_blank" rel="noopener">
          <span data-statuspage-domain="https://2p66nmmycsj3.statuspage.io">all systems operational</span></a>
        </p>
        
        <p>
          Developed and maintained by the Python community, for the Python community.
          <br>
          <a href="https://donate.pypi.org">Donate today!</a>
        </p>
        <p>© 2019 <a href="https://www.python.org/psf/" title="External link" target="_blank" rel="noopener">Python Software Foundation</a></p>
      </div>

      <div class="centered hide-on-desktop">
        <button class="button button--switch-to-desktop hidden" data-target="viewport-toggle.switchToDesktop" data-action="viewport-toggle#switchToDesktop">
          Desktop version
        </button>
      </div>
    </footer>

    

<div class="sponsors">
  <p class="sponsors__title">Supported by</p>
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.elastic.co/">
        <img class="sponsors__image" alt="Elastic" src="/static/images/sponsors/white/elastic.a912fb87.png">
        <span class="sponsors__name">Elastic</span>
        <span class="sponsors__service">Search</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.pingdom.com/">
        <img class="sponsors__image" alt="Pingdom" src="/static/images/sponsors/white/pingdom.07446398.png">
        <span class="sponsors__name">Pingdom</span>
        <span class="sponsors__service">Monitoring</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://cloud.google.com/">
        <img class="sponsors__image" alt="Google" src="/static/images/sponsors/white/google.2f72f26f.png">
        <span class="sponsors__name">Google</span>
        <span class="sponsors__service">BigQuery</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://getsentry.com/for/python">
        <img class="sponsors__image" alt="Sentry" src="/static/images/sponsors/white/sentry.5ab437bc.png">
        <span class="sponsors__name">Sentry</span>
        <span class="sponsors__service">Error logging</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://aws.amazon.com/">
        <img class="sponsors__image" alt="AWS" src="/static/images/sponsors/white/aws.5f800271.png">
        <span class="sponsors__name">AWS</span>
        <span class="sponsors__service">Cloud computing</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.datadoghq.com/">
        <img class="sponsors__image" alt="DataDog" src="/static/images/sponsors/white/datadog.e569d741.png">
        <span class="sponsors__name">DataDog</span>
        <span class="sponsors__service">Monitoring</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.fastly.com/">
        <img class="sponsors__image" alt="Fastly" src="/static/images/sponsors/white/fastly.0563c6f5.png">
        <span class="sponsors__name">Fastly</span>
        <span class="sponsors__service">CDN</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.signalfx.com/">
        <img class="sponsors__image" alt="SignalFx" src="/static/images/sponsors/white/signalfx.560cb5c4.png">
        <span class="sponsors__name">SignalFx</span>
        <span class="sponsors__service">Supporter</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.digicert.com/">
        <img class="sponsors__image" alt="DigiCert" src="/static/images/sponsors/white/digicert.79748718.png">
        <span class="sponsors__name">DigiCert</span>
        <span class="sponsors__service">EV certificate</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://statuspage.io">
        <img class="sponsors__image" alt="StatusPage" src="/static/images/sponsors/white/statuspage.67af0b3d.png">
        <span class="sponsors__name">StatusPage</span>
        <span class="sponsors__service">Status page</span>
      </a>
    
  
</div>

    
  </body>

</html>
"""

soup = BeautifulSoup(html_doc, "lxml")

with open("text.html", "w") as f:
    f.write(soup.prettify())
