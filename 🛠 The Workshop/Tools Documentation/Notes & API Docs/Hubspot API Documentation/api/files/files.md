---
title: "File Manager API Documentation"
description: "Access and test APIs in beta, manage and store files using the HubSpot Files tool."
type: "documentation"
tags:
- "API"
- "HubSpot"
- "File Management"
relationships:
- "#related_to [[Upload a new file]]"
- "#related_to [[List metadata for all files]]"
- "#related_to [[Upload a replacement file]]"
- "#related_to [[Mark a file as deleted]]"
- "#related_to [[Get file metadata]]"
- "#related_to [[Archive a file]]"
- "#related_to [[Hard delete a file and related items]]"
- "#related_to [[Update the access of a group of files]]"
- "#related_to [[Check the status of a file access update task]]"
- "#related_to [[Get a signed URL for a private file]]"
- "#related_to [[Move a file]]"
- "#related_to [[Create a folder]]"
- "#related_to [[List folder metadata]]"
- "#related_to [[Delete a folder]]"
- "#related_to [[Get the folder by ID]]"
createdAt: "2023-06-28T17:56:45.393Z"
---

File Manager
============

.interest-form { padding: 1em; display: none; height: 100%; } .interest-text { padding: 1em; } .hs-form>fieldset{ max-width: 100% !important; }

**Access and test APIs in beta.** 
----------------------------------

**Please note**: This API is currently under development and is subject to change based on testing and feedback. By using these endpoints you agree to adhere to our [Developer Terms](https://legal.hubspot.com/hubspot-developer-terms)& [Developer Beta](https://legal.hubspot.com/developerbetaterms?)Terms. You also acknowledge and understand the risk associated with testing an unstable API. 

 

**This API is currently in beta.** For the latest stable version check out these pages: [Upload a new file](https://legacydocs.hubspot.com/docs/methods/files/v3/upload_new_file), [List metadata for all files](https://legacydocs.hubspot.com/docs/methods/files/get_files), [Upload a replacement file](https://legacydocs.hubspot.com/docs/methods/files/v3/upload_replacement_file), [Mark a file as deleted](https://legacydocs.hubspot.com/docs/methods/files/delete_files_file_id), [Get file metadata](https://legacydocs.hubspot.com/docs/methods/files/get_files_file_id), [Archive a file](https://legacydocs.hubspot.com/docs/methods/files/post_files_file_id_archive), [Hard delete a file and related items](https://legacydocs.hubspot.com/docs/methods/files/hard_delete_file_and_associated_objects), [Update the access of a group of files](https://legacydocs.hubspot.com/docs/methods/files/update_file_access), [Check the status of a file access update task](https://legacydocs.hubspot.com/docs/methods/files/check_accessibility_task_status), [Get a signed URL for a private file](https://legacydocs.hubspot.com/docs/methods/files/get-signed-url-private-file), [Move a file](https://legacydocs.hubspot.com/docs/methods/files/post_files_file_id_move_file), [Create a folder](https://legacydocs.hubspot.com/docs/methods/files/post_folders), [List folder metadata](https://legacydocs.hubspot.com/docs/methods/files/get_folders), [Delete a folder](https://legacydocs.hubspot.com/docs/methods/files/delete_folders_folder_id), [Get the folder by ID](https://legacydocs.hubspot.com/docs/methods/files/get_folders_folder_id),

  
Provide Feedback

hbspt.forms.create({ portalId: "428357", formId: "037350c3-535d-4755-82ca-53b73367754f", cssClass: "hs-form" });

First name

Last name

Email

How satisfied are you with this API beta\*

Please SelectVery satisfiedSatisfiedNeutralUnsatisfiedVery unsatisfied

Can we contact you with follow-up questions about this feedback?

*   Yes, HubSpot can contact me about this feedback 

By selecting “Yes,” you are allowing HubSpot to store any personal information submitted through this form. We respect your privacy and will only use it to contact you if we have follow-up questions about today’s feedback. You can unsubscribe from these communications at any time. For more information, check out our [Privacy Policy.](https://legal.hubspot.com/privacy-policy)

$(document).ready(() => { $("#interest-btn").click(() => { $(".interest-form").toggle(); }); });

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use HubSpot’s files tool to manage and store files in HubSpot. Files hosted in HubSpot can be uploaded and used in both HubSpot and external content. They can also be attached to records using the [engagements API](/docs/api/crm/engagements).

If your company is building its website using HubSpot's CMS, you can use the files API to upload and store assets in HubSpot. These files can then be served and shared through the HubSpot CMS.

You can access the files tool from [within HubSpot](https://knowledge.hubspot.com/files/upload-files-to-use-in-your-hubspot-content) or via the files API. Below, learn about the files API and how to upload and delete files. For a full list of files API endpoints, click the Endpoints tab above.

Upload a file[](https://developers.hubspot.com/docs/api/files/files#upload-a-file)
----------------------------------------------------------------------------------

Files can be uploaded using a multipart/form-data `POST` request to `files/v3/files` with the following fields. While a specific folder ID is not required at upload, it's recommend to upload files into a folder and not the root directory. Folder requirements at upload are subject to change in the future. 

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`file`

 | 

The file to upload (required).

 |
| 

`options`

 | 

A JSON object that controls the file's privacy and indexability, and contains two fields: `access`, which is required, and `ttl`, which specifies a time period after which the file will be automatically deleted.

If you're using the `ttl` field:

*   The minimum period that must be set is 1 day.
*   The maximum period that can be set is 1 year.
*   After the set period,  the file will be permanently deleted. After deletion, the file cannot be recovered or restored.

  
 |
| 

`folderId`

 | 

The ID of the folder that the file will be uploaded to. Either this field or `folderPath` must be provided in your request (but not both).

 |
| 

`folderPath`

 | 

The path of the folder that the file will be uploaded to. Either this field or `folderId` must be provided in your request (but not both).

 |
| 

`fileName`

 | 

The name of the file. If no name is specified, a name will be generated from the file's content.

 |
| 

`charsetHunch`

 | 

Character set encoding for the uploaded file. If not provided, it will be derived from the file.

 |

As an example, if you wanted to upload a file with the following criteria to your HubSpot account:

*   **File name:** `cat.png`
*   **Destination folder in the HubSpot file manager:** `/library/cat_archive`
*   **File accessibility in HubSpot:** privately accessible

The following headers and request body would need to be part of your request:

curl --request POST \\ --url 'https://api.hubapi.com/files/v3/files?=' \\ --header 'Authorization: Bearer pat-na1-00000000-0000-0000-0000-000000000000' \\ --header 'Content-type: multipart/form-data' \\ --form file=@/Users/person/Downloads/cat.png \\ --form 'options={"access": "PRIVATE"}' \\ --form folderPath=/library/cat\_archive

The resulting response will include the `id` and `parentFolderId` of the uploaded file, which you can use to retrieve the file via a GET request.

// 201 Response from successful file upload { "id": "122692044085", "createdAt": "2023-06-28T17:56:45.393Z", "updatedAt": "2023-06-28T17:56:45.393Z", "archived": false, "parentFolderId": "122692510820", "name": "cat", "path": "/library/cat\_archive/cat.png", "size": 24574, "height": 219, "width": 225, "encoding": "png", "type": "IMG", "extension": "png", "defaultHostingUrl": "https://12345.fs1.hubspotusercontent-na1.net/hubfs/12345/library/cat\_archive/cat.png", "url": "https://12345.fs1.hubspotusercontent-na1.net/hubfs/12345/library/cat\_archive/cat.png", "isUsableInContent": true, "access": "PRIVATE" }

Check a file's upload status[](https://developers.hubspot.com/docs/api/files/files#check-a-file-s-upload-status)
----------------------------------------------------------------------------------------------------------------

If you're importing a file from a URL to your file manager using a `POST` request to `files/v3/files/import-from-url/async`, you can review the upload status of the file.

To do so, use a `GET` request to `files/v3/files/import-from-url/async/tasks/{taskId}/status`.

After making this request, you will receive one of the following replies:  

*   `PENDING`: the file is in the queue to be uploaded. The import process has not yet started. 
*   `PROCESSING`: the file is in the process of being uploaded.
*   `CANCELED`: the upload has been canceled and the file will not be uploaded. To import the file to your HubSpot account, you will need to upload the file again.  
*   `COMPLETE`: the file has been uploaded to the files tool successfully. The uploaded file will appear in your files tool.  

View a file's details[](https://developers.hubspot.com/docs/api/files/files#view-a-file-s-details)
--------------------------------------------------------------------------------------------------

To review the details of a file that's been uploaded to the files tool, make a `GET` request to `files/v3/files/{fileId}`. This will return the file with details such as name, height and width, encoding, the URL, and more.

For example, to retrieve the details of a file:  

If a file is set to private, the returned URL will result in a 404 error. To get a viewable URL of the file, you can make a `GET` request to `/files/v3/files/{fileId}/signed-url`. When making this request, you can include `property` parameters to return specific properties such as height and width.

Delete a file[](https://developers.hubspot.com/docs/api/files/files#delete-a-file)
----------------------------------------------------------------------------------

To delete a file, make a `DELETE` request to `files/v3/files/{fileId}`. This will mark the file as deleted and make the content of the file inaccessible.

To permanently delete a file, make a `DELETE` request to `files/v3/files/{fileId}/gdpr-delete`. This will permanently delete the file’s content and metadata within 7 days. 

If a file is not GDPR deleted, its contents will remain on HubSpot's servers in a private state where no one can access it. To ensure file contents are fully deleted, use the GDPR delete functionality. 

Create a folder[](https://developers.hubspot.com/docs/api/files/files#create-a-folder)
--------------------------------------------------------------------------------------

To create a folder, make a `POST` request to `files/v3/folders`. When making the request, you can include the below fields. 

Use this table to describe parameters / fields
| Field | Required | Description |
| --- | --- | --- |
| 
`name`

 | Yes | 

Name of the folder you want to create.

 |
| 

`parentFolderId`

 | No | 

To create the folder within an existing folder, include this field with the existing folder's ID. `parentFolderId` and `parentFolderPath` cannot be set at the same time.

 |
| 

`parentFolderPath`

 | No | 

To create the folder within an existing folder, include this field with the existing folder's path. `parentFolderId` and `parentFolderPath` cannot be set at the same time.

 |

JSON

Copy all

    //Example request body of POST request to /files/v3/folders
    {
      "name": "myNewFolder",
      "parentFolderId": 12345
    }

Changes in v3[](https://developers.hubspot.com/docs/api/files/files#changes-in-v3)
----------------------------------------------------------------------------------

If you’ve been using the previous version of this API, v3 has the following changes:

*   All files uploaded through the API will be visible in the files dashboard and the files picker. Hidden files cannot be created. However, private files and non-indexable files can still be created. 
*   Listing files will not return hidden or deleted files. However, a much broader range of filters can be applied. Hidden files can still be fetched by ID, but require a new scope: `files_ui_hidden.read.`
*   Multiple files cannot be uploaded with a single request. 
*   Folder update actions like moving and renaming are now asynchronous. Each request will return a token that can be used to check the status of the folder edit.
*   Endpoints that create or replace files require you to provide access levels for the files. These access levels are:
    *   `PUBLIC_INDEXABLE`**:** file is publicly accessible by anyone who has the URL. Search engines can index the file.
    *   `PUBLIC_NOT_INDEXABLE`**:** file is publicly accessible by anyone who has the URL. The X-Robots-Tag: noindex header will be sent whenever the file is retrieved, instructing search engines not to index the file.
    *   **`PRIVATE`:** file is not publicly accessible. Requires a signed URL to display content. Search engines cannot index the file.
*   Endpoints that create files allow for a level of duplicate detections as part of the file’s upload options. 
    
    *   `ENTIRE_PORTAL`**:** search for a duplicate file in the account.
    *   `EXACT_FOLDER`**:** search for a duplicate file in the provided folder.
    
    *   `NONE`**:** do not run any duplicate validation.
    *   `REJECT`**:** reject the upload if a duplicate is found.
    *   `RETURN_EXISTING`**:** if a duplicate file is found, do not upload a new file and return the found duplicate instead.
    *   Duplicate detection works on a `duplicateValidationScope`, which affects how we search for a duplicate.
    *   This also requires a `duplicateValidationStrategy`, which dictates what happens if a duplicate is found.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/files/files#page-feedback)
----------------------------------------------------------------------------------------

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