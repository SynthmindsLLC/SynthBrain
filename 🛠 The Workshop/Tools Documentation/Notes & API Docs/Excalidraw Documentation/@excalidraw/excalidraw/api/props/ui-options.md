*   [](/)
*   @excalidraw/excalidraw
*   [API](/docs/@excalidraw/excalidraw/api)
*   [Props](/docs/@excalidraw/excalidraw/api/props/)
*   UIOptions

On this page

UIOptions
=========

This prop can be used to customise UI of Excalidraw. Currently we support customising [`canvasActions`](#canvasactions), [`dockedSidebarBreakpoint`](#dockedsidebarbreakpoint) [`welcomeScreen`](#welcmescreen) and [`tools`](#tools).

    { canvasActions?: CanvasActions,  dockedSidebarBreakpoint?: number,  welcomeScreen?: boolean }

canvasActions[​](#canvasactions "Direct link to heading")
---------------------------------------------------------

This `prop` controls the visibility of the canvas actions inside the `menu`.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `changeViewBackgroundColor` | `boolean` | `true` | Indicates whether to show `Background color picker`. |
| `clearCanvas` | `boolean` | `true` | Indicates whether to show `Clear canvas` button. |
| `export` | `false` | [`exportOpts`](#exportopts) | `object` | This prop allows to customize the UI inside the export dialog. By default it shows the `save file to disk`. For more details visit [`exportOpts`](#exportopts). |
| `loadScene` | `boolean` | `true` | Indicates whether to show `Load` button. |
| `saveToActiveFile` | `boolean` | `true` | Indicates whether to show `Save` button to save to current file. |
| `toggleTheme` | `boolean` | `null` | `null` | Indicates whether to show `Theme toggle`. When defined as `boolean`, takes precedence over [`props.theme`](/docs/@excalidraw/excalidraw/api/props#theme) to show `Theme toggle`. |
| `saveAsImage` | `boolean` | `true` | Indicates whether to show `Save as image` button. |

Live Editor

function App() { const UIOptions = { canvasActions: { changeViewBackgroundColor: false, clearCanvas: false, loadScene: false, }, }; return ( <div style={{ height: "500px" }}> <Excalidraw UIOptions={UIOptions} /> </div> ); }

function App() {

  const UIOptions \= {

    canvasActions: {

      changeViewBackgroundColor: false,

      clearCanvas: false,

      loadScene: false,

    },

  };

  return (

    <div style\={{ height: "500px" }}\>

      <Excalidraw UIOptions\={UIOptions} />

    </div\>

  );

}

/\*\* \* Reset the text fill color so that placeholder is visible \*/ .npm\_\_react-simple-code-editor\_\_textarea:empty { -webkit-text-fill-color: inherit !important; } /\*\* \* Hack to apply on some CSS on IE10 and IE11 \*/ @media all and (-ms-high-contrast: none), (-ms-high-contrast: active) { /\*\* \* IE doesn't support '-webkit-text-fill-color' \* So we use 'color: transparent' to make the text transparent on IE \* Unlike other browsers, it doesn't affect caret color in IE \*/ .npm\_\_react-simple-code-editor\_\_textarea { color: transparent !important; } .npm\_\_react-simple-code-editor\_\_textarea::selection { background-color: #accef7 !important; color: transparent !important; } }

Result

Shapes
------

1

2

3

4

5

6

7

8

9

0

Library

Drawing canvas

### exportOpts[​](#exportopts "Direct link to heading")

The below attributes can be set in `UIOptions.canvasActions.export` to customize the export dialog.  
If `UIOptions.canvasActions.export` is `false` the export button will not be rendered.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `saveFileToDisk` | `boolean` | `true` | Indicates whether `save file to disk` button should be shown |
| `onExportToBackend` | `object` | \_ | This callback is triggered when the shareable-link button is clicked in the export dialog. The link button will only be shown if this callback is passed. |
| `renderCustomUI` | `object` | \_ | This callback should be supplied if you want to render custom UI in the export dialog. |

dockedSidebarBreakpoint[​](#dockedsidebarbreakpoint "Direct link to heading")
-----------------------------------------------------------------------------

This prop indicates at what point should we break to a docked, permanent sidebar. If not passed it defaults to [`MQ_RIGHT_SIDEBAR_MAX_WIDTH_PORTRAIT`](https://github.com/excalidraw/excalidraw/blob/master/packages/excalidraw/constants.ts#L161).  
If the _width_ of the _excalidraw_ container exceeds _dockedSidebarBreakpoint_, the sidebar will be `dockable` and the button to `dock` the sidebar will be shown  
If user choses to `dock` the sidebar, it will push the right part of the UI towards the left, making space for the sidebar as shown below.

![image](https://user-images.githubusercontent.com/11256141/174664866-c698c3fa-197b-43ff-956c-d79852c7b326.png)

Live Editor

function App() { return ( <div style={{ height: "500px" }}> <Excalidraw UIOptions={{dockedSidebarBreakpoint: 200}}/> </div> ); }

function App() {

  return (

    <div style\={{ height: "500px" }}\>

      <Excalidraw UIOptions\={{dockedSidebarBreakpoint: 200}}/>

    </div\>

  );

}

/\*\* \* Reset the text fill color so that placeholder is visible \*/ .npm\_\_react-simple-code-editor\_\_textarea:empty { -webkit-text-fill-color: inherit !important; } /\*\* \* Hack to apply on some CSS on IE10 and IE11 \*/ @media all and (-ms-high-contrast: none), (-ms-high-contrast: active) { /\*\* \* IE doesn't support '-webkit-text-fill-color' \* So we use 'color: transparent' to make the text transparent on IE \* Unlike other browsers, it doesn't affect caret color in IE \*/ .npm\_\_react-simple-code-editor\_\_textarea { color: transparent !important; } .npm\_\_react-simple-code-editor\_\_textarea::selection { background-color: #accef7 !important; color: transparent !important; } }

Result

Shapes
------

1

2

3

4

5

6

7

8

9

0

Library

Drawing canvas

tools[​](#tools "Direct link to heading")
-----------------------------------------

This `prop` controls the visibility of the tools in the editor. Currently you can control the visibility of `image` tool via this prop.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| image | boolean | true | Decides whether `image` tool should be visible. |

[Edit this page](https://github.com/excalidraw/excalidraw/tree/master/dev-docs/docs/@excalidraw/excalidraw/api/props/ui-options.mdx)

[

Previous

Render Props

](/docs/@excalidraw/excalidraw/api/props/render-props)[

Next

Children Components

](/docs/@excalidraw/excalidraw/api/children-components)