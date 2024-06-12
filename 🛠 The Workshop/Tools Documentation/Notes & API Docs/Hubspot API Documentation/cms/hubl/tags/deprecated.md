---
Please provide me with more context. What kind of mission are you writing about? 

For example: "* **Is it a mission statement for a company or organization?** "
* **Is it a mission for a specific project or campaign?**
* **Is it a mission statement for a personal goal?**

Once I know the context, I can give you a better starting point or suggestions for your mission statement.
---

Deprecated HubL Supported Tags


==================================

Last updated: March 10, 2023

The following is a list of HubL supported tags that are deprecated. While these tags still operate as intended, newer tags have been created to replace them that are more streamlined and optimized. These new tags are indicated below. This page is for historical reference. 

Custom Widgets[](https://developers.hubspot.com/docs/cms/hubl/tags/deprecated#custom-widgets)
---------------------------------------------------------------------------------------------

This tag has been replaced by [**custom module tag.**](/docs/cms/hubl/tags#custom-modules)

Follow Me[](https://developers.hubspot.com/docs/cms/hubl/tags/deprecated#follow-me)
-----------------------------------------------------------------------------------

Follow me modules render icons that link to your various social media profiles. The icons that display are based upon your Social Settings.

This tag is replaced by the newer Follow Me default module.

{% follow\_me "follow\_me" %} {% follow\_me "follow\_us" title='Follow Us', module\_title\_tag="h2" %}<span id="hs\_cos\_wrapper\_module\_14162805806361260" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_follow\_me" style="" data-hs-cos-general-type="widget" data-hs-cos-type="follow\_me"> <h2>Follow Us</h2> <div style=""> <a target="\_blank" class="fm\_button fm\_googleplus" href=""><span title="Follow us on Google+"></span></a> <a target="\_blank" class="fm\_button fm\_facebook" href=""><span title="Follow us on Facebook"></span></a> <a target="\_blank" class="fm\_button fm\_twitter" href=""><span title="Follow us on Twitter"></span> </div> </span>

Global Widget[](https://developers.hubspot.com/docs/cms/hubl/tags/deprecated#global-widget)
-------------------------------------------------------------------------------------------

A global widget is one which can be shared across template

The tag has been replaced with the [custom module tag](/docs/cms/hubl/tags#custom-modules).

{% global\_widget "facebook\_fan\_box" overrideable=False, label='Facebook Fan Box' %}"

Google search[](https://developers.hubspot.com/docs/cms/hubl/tags/deprecated#google-search)
-------------------------------------------------------------------------------------------

The Google Search Tag and modules are no longer available. This has been replaced by HubSpot's own native search. 

Image slider[](https://developers.hubspot.com/docs/cms/hubl/tags/deprecated#image-slider)
-----------------------------------------------------------------------------------------

Generates a HubSpot image slider module. This slider module is based on [FlexSlider](http://flexslider.woothemes.com/). While you can create a slider module with standard module HubL syntax, If you want to predefine default slides using HubL, you must use block syntax. Both methods are shown below.

This tag has been deprecated in favor of the [Gallery tag](/docs/cms/hubl/tags#gallery).

{% image\_slider "image\_slider" %} <-- Block syntax --> {% widget\_block image\_slider "crm\_slider" sizing='static', only\_thumbnails=False, transition='slide', caption\_position='below', with\_thumbnail\_nav=False, lightbox=False, auto\_advance=True, overrideable=True, description\_text='', show\_pagination=True, label='Image Slider', loop\_slides=True, num\_seconds=5 %} {% widget\_attribute "slides" is\_json=True %}\[{"caption": "CRM Contacts App", "show\_caption": true, "link\_url": "http://www.hubspot.com/crm", "alt\_text": "Screenshot of CRM Contacts", "img\_src": "http://go.hubspot.com/hubfs/Contacts-View-1.png?t=1430860504240", "open\_in\_new\_tab": true}, {"caption": "HubSpot CRM Contact Profile", "show\_caption": true, "link\_url": "http://www.hubspot.com/", "alt\_text": "HubSpot CRM Contact Profile", "img\_src": "http://cdn2.hubspot.net/hubfs/53/Contact-Profile.png?t=1430860504240", "open\_in\_new\_tab": true}\]{% end\_widget\_attribute %} {% end\_widget\_block %}<span id="hs\_cos\_wrapper\_crm\_slider" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_image\_slider" style="" data-hs-cos-general-type="widget" data-hs-cos-type="image\_slider"> <div id="hs\_cos\_flex\_slider\_crm\_slider" class="hs\_cos\_flex-slider flex-slider-main slider-mode-slider"> <div class="hs\_cos\_flex-viewport" style="overflow: hidden; position: relative;"> <ul class="hs\_cos\_flex-slides hs\_cos\_flex-slides-main " style="width: 800%; -webkit-transition-duration: 0s; transition-duration: 0s; -webkit-transform: translate3d(-1090px, 0px, 0px);"> <li class="hs\_cos\_flex-slide-main clone" aria-hidden="true" style="width: 1090px; float: left; display: block;"> <a href="//www.hubspot.com/" target="\_blank"><img src="//cdn2.hubspot.net/hubfs/53/Contact-Profile.png?t=1430860504240&t=1430335520686" alt="HubSpot CRM Contact Profile" draggable="false"></a> <div class="caption"> HubSpot CRM Contact Profile </div> </li> <li class="hs\_cos\_flex-slide-main hs\_cos\_flex-active-slide" style="width: 1090px; float: left; display: block;"> <a href="//www.hubspot.com/crm" target="\_blank"><img src="http://go.hubspot.com/hubfs/Contacts-View-1.png?t=1430860504240&t=1430335520686" alt="Screenshot of CRM Contacts" draggable="false"></a> <div class="caption"> CRM Contacts App </div> </li> <li class="hs\_cos\_flex-slide-main" style="width: 1090px; float: left; display: block;"> <a href="//www.hubspot.com/" target="\_blank"><img src="//cdn2.hubspot.net/hubfs/53/Contact-Profile.png?t=1430860504240&t=1430335520686" alt="HubSpot CRM Contact Profile" draggable="false"></a> <div class="caption"> HubSpot CRM Contact Profile </div> </li> <li class="hs\_cos\_flex-slide-main clone" aria-hidden="true" style="width: 1090px; float: left; display: block;"> <a href="//www.hubspot.com/crm" target="\_blank"><img src="http://go.hubspot.com/hubfs/Contacts-View-1.png?t=1430860504240&t=1430335520686" alt="Screenshot of CRM Contacts" draggable="false"></a> <div class="caption"> CRM Contacts App </div> </li> </ul> </div> <ol class="hs\_cos\_flex-control-nav hs\_cos\_flex-control-paging"> <li><a class="hs\_cos\_flex-active">1</a></li> <li><a class="">2</a></li> </ol> <ul class="hs\_cos\_flex-direction-nav"> <li><a class="hs\_cos\_flex-prev" href="#">Previous</a></li> <li><a class="hs\_cos\_flex-next" href="#">Next</a></li> </ul> </div> <script> window.hsSliderConfig = window.hsSliderConfig || {}; window.hsSliderConfig\['crm\_slider'\] = { mode: 'slider', mainConfig: { "animationLoop": true, "direction": "horizontal", "slideshowSpeed": 5000.0, "controlNav": true, "smoothHeight": false, "namespace": "hs\_cos\_flex-", "slideshow": true, "selector": ".hs\_cos\_flex-slides > li", "animation": "slide" } }; </script> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`sizing`

 | Enumeration | 

Determines whether the slider changes sizes, based on the height of the slides. Possible values include: "static" or "resize"

 | `"static"` |
| 

`only_thumbnails`

 | Boolean | 

Display images as thumbnails instead of a slider.

 | `False` |
| 

`transition`

 | Enumeration | 

Sets the type of slide transition. Possible values include: "fade" or "slide"

 | `"slide"` |
| 

`caption_position`

 | Enumeration | 

Affects positioning of caption on or below the slide. Possible values include "below" or "superimpose"

 | `"below"` |
| 

`with_thumbnail_nav`

 | Boolean | 

Include thumbnails below slider for navigation (only\_thumbnails must be False for this to be True)

 | `False` |
| 

`lightbox`

 | Boolean | 

Displays thumbnail image in lightbox, when clicked (with\_thumbnail\_nav must be True for this to be True)

 | `False` |
| 

`auto_advance`

 | Boolean | 

Automatically advance slides after the time set in num\_seconds

 | `False` |
| 

`show_pagination`

 | Boolean | 

Provide buttons below slider to randomly navigate among slides

 | `True` |
| 

`label`

 | String | 

A label for this module, visible in the editor only

 | `"Image Slider"` |
| 

`loop_slides`

 | Boolean | 

When True, continuously loop through slides

 | `True` |
| 

`num_seconds`

 | Number | 

Time in seconds to pause between slides

 | `5` |
| 

`slides`

 | JSON | 

A JSON list of the default caption, the link url, the alt text, the image src, and whether to open in a new tab. See block syntax above.

 |  |

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/tags/deprecated#page-feedback)
-------------------------------------------------------------------------------------------------

Was this article helpful? Yes No

Thanks for letting us know. How would you describe this article?

 Inaccurate: it doesn’t reflect what I see in the product

 Unclear: it’s difficult to understand

 Missing information: it’s not comprehensive enough

 Irrelevant: it doesn’t match what I searched for

Great! Is there anything we could change to make it even more helpful? Is there anything we could change to make this article helpful?

 Allow HubSpot to contact me about my documentation feedback.

Email address

Only used if we need clarification on your feedback.

 

Thank you for your feedback, it means a lot to us.

Sorry this feedback form requires JavaScript to function.

This form is used for documentation feedback only. Learn how to [get help with HubSpot](https://knowledge.hubspot.com/account/get-help-with-hubspot).