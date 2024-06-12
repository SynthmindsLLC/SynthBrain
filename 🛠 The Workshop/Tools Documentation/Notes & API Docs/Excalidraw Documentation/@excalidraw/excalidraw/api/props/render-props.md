*   [](/)
*   @excalidraw/excalidraw
*   [API](/docs/@excalidraw/excalidraw/api)
*   [Props](/docs/@excalidraw/excalidraw/api/props/)
*   Render Props

On this page

Render Props
============

renderTopRightUI[​](#rendertoprightui "Direct link to heading")
---------------------------------------------------------------

    (isMobile: boolean, appState:AppState) => JSX | null

A function returning `JSX` to render `custom` UI in the top right corner of the app.

Live Editor

function App() { return ( <div style={{ height: "500px" }}> <Excalidraw renderTopRightUI={() => { return ( <button style={{ background: "#70b1ec", border: "none", color: "#fff", width: "max-content", fontWeight: "bold", }} onClick={() => window.alert("This is dummy top right UI")} > Click me </button> ); }} /> </div> ); }

function App() {

  return (

    <div style\={{ height: "500px" }}\>

      <Excalidraw

        renderTopRightUI={() \=> {

          return (

            <button

              style\={{

                background: "#70b1ec",

                border: "none",

                color: "#fff",

                width: "max-content",

                fontWeight: "bold",

              }}

              onClick\={() \=> window.alert("This is dummy top right UI")}

            \>

              Click me

            </button\>

          );

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

Click me

Library

Drawing canvas

renderCustomStats[​](#rendercustomstats "Direct link to heading")
-----------------------------------------------------------------

A function that can be used to render custom stats (returns JSX) in the `nerd stats` dialog.

![Nerd Stats](/assets/images/nerd-stats-275925684149f752e3f5487f11105f12.png)

For example you can use this prop to render the size of the elements in the storage as do in [excalidraw.com](https://excalidraw.com).

Live Editor

function App() { return ( <div style={{ height: "500px" }}> <Excalidraw renderCustomStats={() => ( <p style={{ color: "#70b1ec", fontWeight: "bold" }}> Dummy stats will be shown here </p> )} /> </div> ); }

function App() {

  return (

    <div style\={{ height: "500px" }}\>

      <Excalidraw

        renderCustomStats\={() \=> (

          <p style\={{ color: "#70b1ec", fontWeight: "bold" }}\>

            Dummy stats will be shown here

          </p\>

        )}

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

renderEmbeddable[​](#renderembeddable "Direct link to heading")
---------------------------------------------------------------

    (element: NonDeleted<ExcalidrawEmbeddableElement>, appState: AppState) => JSX.Element | null

Allows you to replace the renderer for embeddable elements (which renders `<iframe>` elements).

| Parameter | Type | Description |
| --- | --- | --- |
| `element` | `NonDeleted<ExcalidrawEmbeddableElement>` | The embeddable element to be rendered. |
| `appState` | `AppState` | The current state of the UI. |

[Edit this page](https://github.com/excalidraw/excalidraw/tree/master/dev-docs/docs/@excalidraw/excalidraw/api/props/render-props.mdx)

[

Previous

excalidrawAPI

](/docs/@excalidraw/excalidraw/api/props/excalidraw-api)[

Next

UIOptions

](/docs/@excalidraw/excalidraw/api/props/ui-options)