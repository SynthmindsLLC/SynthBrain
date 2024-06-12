*   [](/)
*   @excalidraw/excalidraw
*   [API](/docs/@excalidraw/excalidraw/api)
*   [Children Components](/docs/@excalidraw/excalidraw/api/children-components)
*   LiveCollaborationTrigger

LiveCollaborationTrigger
========================

If you implement live collaboration support and want to expose the same UI button as on [excalidraw.com](https://excalidraw.com), you can render the `<LiveCollaborationTrigger/>` component using the [renderTopRightUI](/docs/@excalidraw/excalidraw/api/props#rendertoprightui) prop.

You'll need to supply `onSelect()` to handle opening of your collaboration dialog, but the button will display `appState.collaborators` count provided you have supplied it.

| Prop | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `onSelect` | `function` | Yes |  | Handler called when the user clicks on the button |
| `isCollaborating` | `boolean` | Yes | false | Whether live collaboration session is in effect. Modifies button style. |

Live Editor

function App() { const \[excalidrawAPI, setExcalidrawAPI\] = useState(null); const \[isCollaborating, setIsCollaborating\] = useState(false); return ( <div style={{ height: "500px" }}> <p style={{ fontSize: "16px" }}> Selecting the checkbox to see the collaborator count </p> <label style={{ fontSize: "16px", fontWeight: "bold" }}> <input type="checkbox" checked={isCollaborating} onChange={() => { if (!isCollaborating) { const collaborators = new Map(); collaborators.set("id1", { username: "Doremon", avatarUrl: "../../../../img/doremon.png", }); collaborators.set("id3", { username: "Pika", avatarUrl: "../../../../img/pika.jpeg", }); excalidrawAPI.updateScene({ collaborators }); } else { excalidrawAPI.updateScene({ collaborators: new Map(), }); } setIsCollaborating(!isCollaborating); }} /> Show Collaborators </label> <Excalidraw ref={(api) => setExcalidrawAPI(api)} renderTopRightUI={() => ( <LiveCollaborationTrigger isCollaborating={isCollaborating} onSelect={() => { window.alert("You clicked on collab button"); setIsCollaborating(true); }} /> )} ></Excalidraw> </div> ); }

function App() {

  const \[excalidrawAPI, setExcalidrawAPI\] \= useState(null);

  const \[isCollaborating, setIsCollaborating\] \= useState(false);

  return (

    <div style\={{ height: "500px" }}\>

      <p style\={{ fontSize: "16px" }}\>

        Selecting the checkbox to see the collaborator count

      </p\>

      <label style\={{ fontSize: "16px", fontWeight: "bold" }}\>

        <input

          type="checkbox"

          checked={isCollaborating}

          onChange={() \=> {

            if (!isCollaborating) {

              const collaborators \= new Map();

              collaborators.set("id1", {

                username: "Doremon",

                avatarUrl: "../../../../img/doremon.png",

              });

              collaborators.set("id3", {

                username: "Pika",

                avatarUrl: "../../../../img/pika.jpeg",

              });

              excalidrawAPI.updateScene({ collaborators });

            } else {

              excalidrawAPI.updateScene({

                collaborators: new Map(),

              });

            }

            setIsCollaborating(!isCollaborating);

          }}

        />

        Show Collaborators

      </label\>

      <Excalidraw

        ref\={(api) \=> setExcalidrawAPI(api)}

        renderTopRightUI\={() \=> (

          <LiveCollaborationTrigger

            isCollaborating\={isCollaborating}

            onSelect\={() \=> {

              window.alert("You clicked on collab button");

              setIsCollaborating(true);

            }}

          />

        )}

      \></Excalidraw\>

    </div\>

  );

}

/\*\* \* Reset the text fill color so that placeholder is visible \*/ .npm\_\_react-simple-code-editor\_\_textarea:empty { -webkit-text-fill-color: inherit !important; } /\*\* \* Hack to apply on some CSS on IE10 and IE11 \*/ @media all and (-ms-high-contrast: none), (-ms-high-contrast: active) { /\*\* \* IE doesn't support '-webkit-text-fill-color' \* So we use 'color: transparent' to make the text transparent on IE \* Unlike other browsers, it doesn't affect caret color in IE \*/ .npm\_\_react-simple-code-editor\_\_textarea { color: transparent !important; } .npm\_\_react-simple-code-editor\_\_textarea::selection { background-color: #accef7 !important; color: transparent !important; } }

Result

Selecting the checkbox to see the collaborator count

Show Collaborators

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

[Edit this page](https://github.com/excalidraw/excalidraw/tree/master/dev-docs/docs/@excalidraw/excalidraw/api/children-components/live-collaboration-trigger.mdx)

[

Previous

Footer

](/docs/@excalidraw/excalidraw/api/children-components/footer)[

Next

Utils

](/docs/@excalidraw/excalidraw/api/utils)