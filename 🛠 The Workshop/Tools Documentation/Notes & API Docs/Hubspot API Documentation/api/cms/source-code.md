---
title: "CMS Source Code API"
description: "The CMS Source Code API allows you to interact with the files stored in your HubSpot Developer File System, including templates, modules, CSS, JS, and other CMS assets. You can upload new files or changes, download or delete CMS assets, fetch metadata for each file or folder, validate file contents, and more."
type: "work"
tags:
- "HubSpot"
- "API"
- "CMS"
relationships:
- "#part_of [[HubSpot Developer File System]]"
- "#used_for [[Design Manager]]"
- "#related_to [[HubSpot CMS]]"
- "#related_to [[HubL]]"
environment: "published"
path: "/cms/v3/source-code/published/content/overview.html"
---

CMS Source Code
===============

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Basic Features[](https://developers.hubspot.com/docs/api/cms/source-code#basic-features)
----------------------------------------------------------------------------------------

The CMS Source Code API allows you to interact with the files stored in your HubSpot [Developer File System](https://developers.hubspot.com/docs/cms/key-concepts#developer-file-system). These files include all of the templates, modules, CSS, JS, and other CMS assets seen in the Design Manager. Through this API, you can:

*   Upload new files to their HubSpot account, or upload changes to existing files.
*   Download or delete CMS assets from their account.
*   Fetch metadata for each file or folder in the Design Manager.
*   Validate file contents for use in HubSpot CMS, including HubL syntax.
*   Upload zip files as file packages and extract them inside the account.

With this API you can edit all your CMS assets locally as well as build tooling to help you move even faster. 

Environment and path[](https://developers.hubspot.com/docs/api/cms/source-code#environment-and-path)
----------------------------------------------------------------------------------------------------

The Source Code API endpoints use the `environment` and `path` parameters to identify files in the CMS Developer File System. These parameters are generally specified in the endpoint path itself, as in `/cms/v3/source-code/{environment}/content/{path}`.

The `environment` parameter refers to whether you are interacting with the unpublished or live version of each file. For unpublished changes, use `draft`. For live changes, use `published`.

Note that uploading to `published` is equivalent to pressing the “Publish” button in the Design Manager. As such, whatever is currently in `draft` will be cleared.

The `path` parameter refers to the location of the file in the CMS Developer File System. Top level assets are not preceded by a `/` character as you would see in a UNIX based operating system. When uploading a new file, this should be the desired location where the file should be created. When retrieving or uploading changes to an existing file, this should match the path of the existing file.  
  
We use the local file formats for all asset types, which means that certain types of assets are broken up into multiple files. For instance, a module is actually represented as a directory ending in the `.module` suffix, so to retrieve the HTML for a module, one would need to use the path `foo.module/module.html`. See the [local development documentation](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli) for further information.

Downloading a file[](https://developers.hubspot.com/docs/api/cms/source-code#downloading-a-file)
------------------------------------------------------------------------------------------------

To download a file from your HubSpot account, make a `GET` request to `/cms/v3/source-code/{environment}/content/{path}` and set the header to `Accept: application/octet-stream`.

File data will be downloaded in binary format. You cannot download the entire contents of a folder. Instead, you must fetch the folder metadata and retrieve each of its children individually.

Fetching file and folder metadata[](https://developers.hubspot.com/docs/api/cms/source-code#fetching-file-and-folder-metadata)
------------------------------------------------------------------------------------------------------------------------------

To fetch file and folder metadata, such as path, filename, and created/updated timestamps, make a `GET` request to `/cms/v3/source-code/{environment}/metadata/{path}` and set the header to `Accept: application/json`. 

File and folder metadata will be returned in a JSON object:

*   Folder metadata will be indicated by the `folder: true` property.
*   The `children` array will show the names of files and subfolders within the folder. These filenames can be used to traverse the folder tree: simply fetch one folder metadata and recursively fetch the children of the folder and all subfolders.

Uploading a file[](https://developers.hubspot.com/docs/api/cms/source-code#uploading-a-file)
--------------------------------------------------------------------------------------------

To upload a local file to your HubSpot account, make a `PUT` request to `/cms/v3/source-code/{environment}/content/{path}`. You must upload the file using the `multipart/form-data` content type, and the binary file data must be included as a field named `file`.

For example:

*   **Uploading a new file:**  
    PUT `/cms/v3/source-code/published/content/my-new-file.html`  
    `Content-Type: multipart/form-data`  
    `Form Data: { file: [_binary file data_] }`
*   **Updating an existing file draft:**  
    PUT `/cms/v3/source-code/draft/content/path/to/existing-file.html`  
    `Content-Type: multipart/form-data`  
    `Form Data: { file: [_binary file data_] }`

HubSpot currently supports the following file types:

*   `css`
*   `js`
*   `json`
*   `html`
*   `txt`
*   `md`
*   `jpg`
*   `jpeg`
*   `png`
*   `gif`
*   `map`
*   `svg`
*   `ttf`
*   `woff`
*   `woff2`
*   `zip`

Validating file contents[](https://developers.hubspot.com/docs/api/cms/source-code#validating-file-contents)
------------------------------------------------------------------------------------------------------------

To validate the contents of a local file, make a `POST` request to `/cms/v3/source-code/{environment}/validate/{path}`. You must upload the file using the `multipart/form-data` content type, and the binary file data must be included as a field named `file`.

This can be used to validate HubL in a template/module or JSON for a theme or module. If there are validation errors, you will receive a `400` response with the list of relevant errors. These are the same warnings and errors you would see within the design manager.

Note that invalid files will be rejected if you try and publish them directly. It is recommended to validate files first before publishing.

**For example:**  
POST `/cms/v3/source-code/published/validate/my-file.html`  
`Content-Type: multipart/form-data`  
`Form Data: { file: [_binary file data_] }`

Deleting a file[](https://developers.hubspot.com/docs/api/cms/source-code#deleting-a-file)
------------------------------------------------------------------------------------------

To delete a file, make a `DELETE` request to `/cms/v3/source-code/{environment}/content/{path}`.   
  
Deleting from the `published` environment will remove the file entirely, while deleting from the `draft` environment will simply clear out any unpublished changes. Note that deleting published files will immediately impact live content if used anywhere, so make sure to remove all existing references to the file before deleting.

Extracting a file package[](https://developers.hubspot.com/docs/api/cms/source-code#extracting-a-file-package)
--------------------------------------------------------------------------------------------------------------

To extract a zip file, make a `POST` request to `/cms/v3/source-code/extract/{path}`.  
  
The `path` must be a zip file already uploaded to the account. The extraction process is asynchronous and can take up to a minute depending on how many and how large the compressed files are. The contents of the zip are extracted in place to the same folder that contains the zip file, and the original zip file is not deleted automatically upon successful extraction.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/cms/source-code#page-feedback)
--------------------------------------------------------------------------------------------

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