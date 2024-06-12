*   [](/)
*   @excalidraw/excalidraw
*   [API](/docs/@excalidraw/excalidraw/api)
*   [Props](/docs/@excalidraw/excalidraw/api/props/)
*   initialData

initialData
===========

    { elements?: ExcalidrawElement[], appState?: AppState }

This helps to load Excalidraw with `initialData`. It must be an object or a [promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise) which resolves to an object containing the below optional fields.

| Name | Type | Description |
| --- | --- | --- |
| `elements` | [ExcalidrawElement\[\]](https://github.com/excalidraw/excalidraw/blob/master/packages/excalidraw/element/types.ts#L114) | The `elements` with which `Excalidraw` should be mounted. |
| `appState` | [AppState](https://github.com/excalidraw/excalidraw/blob/master/packages/excalidraw/types.ts#L95) | The `AppState` with which `Excalidraw` should be mounted. |
| `scrollToContent` | `boolean` | This attribute indicates whether to `scroll` to the nearest element to center once `Excalidraw` is mounted. By default, it will not scroll the nearest element to the center. Make sure you pass `initialData.appState.scrollX` and `initialData.appState.scrollY` when `scrollToContent` is false so that scroll positions are retained |
| `libraryItems` | [LibraryItems](https://github.com/excalidraw/excalidraw/blob/master/packages/excalidraw/types.ts#L247) | Promise<[LibraryItems](https://github.com/excalidraw/excalidraw/blob/master/packages/excalidraw/types.ts#L200)\> | This library items with which `Excalidraw` should be mounted. |
| `files` | [BinaryFiles](https://github.com/excalidraw/excalidraw/blob/master/packages/excalidraw/types.ts#L82) | The `files` added to the scene. |

You might want to use this when you want to load excalidraw with some initial elements and app state.

Live Editor

function App() { return ( <div style={{ height: "500px" }}> <Excalidraw initialData={{ elements: \[ { type: "rectangle", version: 141, versionNonce: 361174001, isDeleted: false, id: "oDVXy8D6rom3H1-LLH2-f", fillStyle: "hachure", strokeWidth: 1, strokeStyle: "solid", roughness: 1, opacity: 100, angle: 0, x: 100.50390625, y: 93.67578125, strokeColor: "#000000", backgroundColor: "transparent", width: 186.47265625, height: 141.9765625, seed: 1968410350, groupIds: \[\], }, \], appState: { zenModeEnabled: true, viewBackgroundColor: "#a5d8ff" }, scrollToContent: true }} /> </div> ); }

function App() {

  return (

    <div style\={{ height: "500px" }}\>

      <Excalidraw

        initialData\={{

          elements: \[

            {

              type: "rectangle",

              version: 141,

              versionNonce: 361174001,

              isDeleted: false,

              id: "oDVXy8D6rom3H1-LLH2-f",

              fillStyle: "hachure",

              strokeWidth: 1,

              strokeStyle: "solid",

              roughness: 1,

              opacity: 100,

              angle: 0,

              x: 100.50390625,

              y: 93.67578125,

              strokeColor: "#000000",

              backgroundColor: "transparent",

              width: 186.47265625,

              height: 141.9765625,

              seed: 1968410350,

              groupIds: \[\],

            },

          \],

          appState: { zenModeEnabled: true, viewBackgroundColor: "#a5d8ff" },

          scrollToContent: true

        }}

      />

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

[Edit this page](https://github.com/excalidraw/excalidraw/tree/master/dev-docs/docs/@excalidraw/excalidraw/api/props/initialdata.mdx)

[

Previous

Props

](/docs/@excalidraw/excalidraw/api/props/)[

Next

excalidrawAPI

](/docs/@excalidraw/excalidraw/api/props/excalidraw-api)