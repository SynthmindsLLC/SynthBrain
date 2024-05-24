Write module and theme fields using JavaScript


==================================================

Last updated: March 19, 2024

Typically, module and theme fields are configured in a `fields.json` file. However, if you prefer to not use JSON, you can configure your fields with a JavaScript file instead. Writing fields with JavaScript enables you to abstract fields that you use often, dynamically generate new fields, and more easily update existing fields. 

For example, when building a set of modules, you can abstract your module fields into partials which are then pulled into individual modules. By building modules that pull from one source of truth, you’ll no longer need to update those common fields in each module individually. 

Below, learn how to write fields using JavaScript, including the necessary CLI commands, along with some examples to get you started.

Overview[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#overview)
------------------------------------------------------------------------------------------------------------------

At a high level, to write fields using JavaScript:

*   In the module folder or project root, include a JavaScript fields file within a module folder or project root instead of the `fields.json` file. You can use any of the following extensions:
    *   `fields.js` 
    *   `fields.cjs`
    *   `fields.mjs` (requires Node 13.2.0+ to be installed).
*   Optionally, check your JavaScript before uploading to HubSpot by running `hs cms convert-fields`, which will save the output of the fields file locally as `fields.output.json`.
*   Upload the asset to HubSpot through the CLI by running `hs upload` or `hs watch` with a `--convertFields` flag. On upload, HubSpot will convert the JavaScript file to a `fields.json` file.

**Please note:** when HubSpot converts the JavaScript file into the `fields.json` file, it does not store the original JavaScript file. To maintain a source of truth, it's recommended to use a version control system like Git. 

Requirements[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#requirements)
--------------------------------------------------------------------------------------------------------------------------

To use a JavaScript field file to generate fields:

*   The JavaScript fields file must be contained in a module folder or at the project root to be treated as the global `fields.json` file. 
*   The module or theme must not also include a `fields.json` file. Including both will prompt you to select one or the other at upload.
*   The JavaScript fields file must export a function as its default export. The exported function can accept an array of strings called `fieldOptions`, and must return an array of objects. Each entry in the returned array must be one of the following:

1.  A JavaScript object with [valid field key-value pairs](/docs/cms/building-blocks/module-theme-fields).
2.  A JavaScript object with a `.toJSON()` method. When run, this method must return a value that meets criterion 1.
3.  A `Promise` that resolves to a JavaScript object that meets criterion 1.

CLI commands[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#cli-commands)
--------------------------------------------------------------------------------------------------------------------------

Use the following CLI commands when writing module fields with JavaScript.

### Check JavaScript file locally

Check your work locally by running `hs cms convert-fields`, which saves the output of your JavaScript fields file as `fields.output.json` in the same directory as the JavaScript fields file.

`hs cms convert-fields` accepts the following flags:

Use this table to describe parameters / fields
| Flag | Description |
| --- | --- |
| 
`--src`

 | 

The location of the JavaScript fields file, or a directory.

 |
| 

`--fieldOptions=[options]`

 | 

Accepts a space-separated list that will then be passed to every exported JavaScript fields function as an array before compile-time.

For example, you can configure fields to have different labels depending on whether a `--fieldOptions=qa` flag is set.

[View an example of this below](#change-fields-based-on-passed-options).

 |

### Upload to HubSpot

Upload to HubSpot to begin the process of converting the JavaScript file to a `fields.json` file by running either `hs upload` or `hs watch`. 

`hs upload` and `hs watch` accept the following flags:

Use this table to describe parameters / fields
| Flag | Description |
| --- | --- |
| 
`--convertFields`

 | 

Enables JavaScript fields functionality.

 |
| 

`--saveOutput`

 | 

Saves the JavaScript fields file output as `fields.output.json` in the same directory as the JavaScript fields file. If not included, HubSpot will save the output of the JavaScript fields file to a temporary directory then delete it after upload.

 |
| 

`--fieldOptions=[options]`

 | 

Accepts a space-separated list that will then be passed to every exported JavaScript fields function as an array before compile-time.

For example, you can configure fields to have different labels depending on whether a `--fieldOptions=qa` flag is set.

[View an example of this below](#change-fields-based-on-passed-options).

 |

Examples[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#examples)
------------------------------------------------------------------------------------------------------------------

Below, review examples of using JavaScript to write fields files.

### Regular object[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#regular-object)

The following `fields.js` file writes a regular object:

module.exports = (fieldOptions) => { return \[ { required: true, locked: false, help\_text: "", inline\_help\_text: "", name: "button\_text", label: "Button text", type: "text", default: "Add a button link here" } \] }

### Common fields[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#common-fields)

The following `fields.js` file creates a set of common fields to be used across multiple modules:

const setFieldParams = (field, params) => { return {...field, ...params} } const defaultRichTextField = { type: "richtext", enabled\_features: \[ "font\_size", "standard\_emphasis", "block", "font\_family", "alignment" \], display\_width: null, required: false, locked: false } module.exports = (fieldOptions) => { let fields = \[ setFieldParams(defaultRichTextField, { name: "tier", label: "Product tier", default: "<h2>Free</h2>" }), setFieldParams(defaultRichTextField, { name: "description", label: "Product description", default: "<p>For teams that need additional security, control, and support.</p>" }) \] return fields }

### Change fields based on passed options[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#change-fields-based-on-passed-options)

The following `fields.js` file changes the module's fields based on whether the

`--fieldOptions=[qa]` flag was included when running `hs cms convert-fields`, `hs upload`, or `hs watch`:

module.exports = (fieldOptions) => { let fields = \[...\] if(fieldOptions.includes('qa')) { fields = fields.map((field) => { field\["name"\] += "\_qa"; return field; }) } } return fields }

### Add JSON from other files[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#add-json-from-other-files)

The following `fields.js` file includes styles from a `styles.json` file:

const fs = require('fs') module.exports = (fieldOptions) => { const fields = \[...\] const styles = JSON.parse(fs.readFileSync('../../json/styles.json')) return \[fields, styles\] }

### Make async calls[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#make-async-calls)

The following `fields.js` file includes an asynchronous call by setting the exported function as `async`. If you return a Promise, the CLI will wait for the Promise to resolve before writing the `fields.json` file.

module.exports = async (fieldOptions) => { const httpField = fetch('https://example.org/example.json').then(resp => resp.json()) return \[ httpField \] }

### Use external field object libraries[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#use-external-field-object-libraries)

The following `fields.js` file includes an external library. Libraries such as [@iGoMoon/hubspot-fields-js](https://github.com/iGoMoon/hubspot-tools/tree/main/packages/hubspot-fields-js) are supported, as their fields objects expose a `.toJSON()` function. 

const { Field, Group } = require('@iGoMoon/hubspot-fields-js') module.exports = (fieldOptions) => { return \[ Field.text() .name('button\_text', 'Button text') .required(true) .default('Add a button link here'), new Group().children(\[ Field.boolean() .id('1') .name('enable', 'Enable Field') .set('display', 'toggle') .default(true), Field.number().name('number', 'Number Fields'), Field.text() .name('css\_class\_name', 'CSS Class') .set('validation\_regex', '-?\[a-zA-Z\]+\[a-zA-Z0-9- \]+') .inlineHelpText('Enter a CSS class for additional styling'), \]) \] }

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/modules/write-fields-using-javascript#page-feedback)
----------------------------------------------------------------------------------------------------------------------------------

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