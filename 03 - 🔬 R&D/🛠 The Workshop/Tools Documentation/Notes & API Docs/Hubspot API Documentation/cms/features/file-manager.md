File Manager


================

Last updated: May 24, 2023

In addition to the developer file system, HubSpot's file manager can be used to store and serve files. Files in the file manager are served over HubSpot's global content delivery network (CDN).

By default, all files uploaded to the file manager are publicly accessible and may be indexed in search engines. After uploading your files, you can [manage your file's visibility settings](https://knowledge.hubspot.com/files/organize-edit-and-delete-files#edit-your-file-s-visibility-settings) to prevent files from being indexed or accessed. 

The File Manager can be found at [**Marketing > File and Templates > Files**](https://app.hubspot.com/l/files/) in the top navigation menu.

![](https://developers.hubspot.com/hubfs/image-png-May-24-2023-05-49-31-9738-AM.png)   

When to use the File Manager[](https://developers.hubspot.com/docs/cms/features/file-manager#when-to-use-the-file-manager)
--------------------------------------------------------------------------------------------------------------------------

Generally, the file manager should be used for files intended to be utilized in file pickers throughout HubSpot. For example, when selecting an image in an image or rich text module. 

Before uploading files for use with the file manager:

*   Certain [file size and type limits](https://knowledge.hubspot.com/files/supported-file-types#files-tool) will apply. Learn more about [what to consider before uploading files](https://knowledge.hubspot.com/files/upload-files-to-use-in-your-hubspot-content#before-you-get-started) to the file manager.
*   Files uploaded to the file manager cannot be edited within the HubSpot app, other than minor image file editing.
*   If you intend to edit text-based files, they must be stored in the design manager.
*   Text-based files uploaded to the file manager will not be minified or modified in any way. To take advantage of HubSpot’s [JavaScript minification](/docs/cms/developer-reference/cdn#javascript-minification) and [CSS minification and combination](/docs/cms/developer-reference/cdn), store these files in the design manager. 

Uploading files to the File Manager[](https://developers.hubspot.com/docs/cms/features/file-manager#uploading-files-to-the-file-manager)
----------------------------------------------------------------------------------------------------------------------------------------

Files can be uploaded to the file manager via the following options:

*   To upload files directly in HubSpot, learn how to [upload files to the file manager](https://knowledge.hubspot.com/files/upload-files-to-use-in-your-hubspot-content). 
*   To upload files through the [CMS CLI,](/docs/cms/developer-reference/local-development-cms-cli) use the `hs upload filemanager` command. 
*   To upload files using an API, learn more about [HubSpot's _Upload a new file_ API](https://legacydocs.hubspot.com/docs/methods/files/v3/upload_new_file). 

After uploading your files to the file manager, learn how to [organize and manage your files and file details](https://knowledge.hubspot.com/files/organize-edit-and-delete-files). 

Using File Manager files[](https://developers.hubspot.com/docs/cms/features/file-manager#using-file-manager-files)
------------------------------------------------------------------------------------------------------------------

Files uploaded to the file manager can be accessed via the following options:

*    Files uploaded to the file manager are accessible in the various file pickers throughout HubSpot and HubSpot's CMS, such as in rich text or image modules on pages.
*   Files uploaded to the file manager can be accessed through a direct download link. Learn how to [retrieve a file's direct download link](https://knowledge.hubspot.com/files/provide-a-direct-download-link-to-a-file-hosted-on-the-files-tool). 

Optimizations[](https://developers.hubspot.com/docs/cms/features/file-manager#optimizations)
--------------------------------------------------------------------------------------------

File Manager files are automatically [cached](/docs/cms/developer-reference/cdn#browser-and-server-caching), [compressed and resized to be served efficiently](/docs/cms/developer-reference/cdn#image-compression-optimization-and-automatic-image-resizing) and [accessible across all of your hosted domains to reduce cross-origin requests](/docs/cms/developer-reference/cdn#domain-rewriting). Learn more about the HubSpot CMS [CDN, Security, and Performance](/docs/cms/developer-reference/cdn).  
  

Serving HTML and JS files from the file manager[](https://developers.hubspot.com/docs/cms/features/file-manager#serving-html-and-js-files-from-the-file-manager)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

HTML and JavaScript files uploaded to the File Manager and served using a default HubSpot domain to serve files (i.e. `f.hubspotusercontentXX.net`), use Content Type: `text/plain` . This means web browsers will not render and evaluate the code.

If a user goes directly to an HTML file there it will display the HTML code itself to the user. To avoid this, you must serve these files from one of your connected domains instead of a HubSpot default domain.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/features/file-manager#page-feedback)
--------------------------------------------------------------------------------------------------

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