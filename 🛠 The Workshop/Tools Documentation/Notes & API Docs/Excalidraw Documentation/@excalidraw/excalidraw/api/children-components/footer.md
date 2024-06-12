*   [](/)
*   @excalidraw/excalidraw
*   [API](/docs/@excalidraw/excalidraw/api)
*   [Children Components](/docs/@excalidraw/excalidraw/api/children-components)
*   Footer

Footer
======

Earlier we were using `renderFooter` prop to render custom footer which was removed in [#5970](https://github.com/excalidraw/excalidraw/pull/5970). Now you can pass a `Footer` component instead to render the custom UI for footer.

You will need to import the `Footer` component from the package and wrap your component with the Footer component. The `Footer` should a valid React Node.

**Usage**

Live Editor

function App() { return ( <div style={{ height: "500px"}}> <Excalidraw> <Footer> <button className="custom-footer" onClick={() => alert("This is dummy footer")} > custom footer </button> </Footer> </Excalidraw> </div> ); }

function App() {

  return (

    <div style\={{ height: "500px"}}\>

      <Excalidraw\>

        <Footer\>

          <button

            className\="custom-footer"

            onClick\={() \=> alert("This is dummy footer")}

          \>

            custom footer

          </button\>

        </Footer\>

      </Excalidraw\>

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

This will only for `Desktop` devices.

For `mobile` you will need to render it inside the [MainMenu](#mainmenu). You can use the [`useDevice`](#useDevice) hook to check the type of device, this will be available only inside the `children` of `Excalidraw` component.

Open the `Menu` in the below playground and you will see the `custom footer` rendered.

Live Editor

const MobileFooter = ({}) => { const device = useDevice(); if (device.editor.isMobile) { return ( <Footer> <button className="custom-footer" style= {{ marginLeft: '20px', height: '2rem'}} onClick={() => alert("This is custom footer in mobile menu")} > custom footer </button> </Footer> ); } return null; }; const App = () => ( <div style={{ height: "400px" }}> <Excalidraw> <MainMenu> <MainMenu.Item> Item1 </MainMenu.Item> <MainMenu.Item> Item 2 </MainMenu.Item> <MobileFooter /> </MainMenu> </Excalidraw> </div> ); // Need to render when code is span across multiple components // in Live Code blocks editor render(<App />);

const MobileFooter \= ({}) \=> {

  const device \= useDevice();

  if (device.editor.isMobile) {

    return (

      <Footer\>

        <button

          className="custom-footer"

          style= {{ marginLeft: '20px', height: '2rem'}}

          onClick={() \=> alert("This is custom footer in mobile menu")}

        >

          custom footer

        </button\>

      </Footer\>

    );

  }

  return null;

};

const App \= () \=> (

  <div style\={{ height: "400px" }}\>

    <Excalidraw\>

      <MainMenu\>

        <MainMenu.Item\> Item1 </MainMenu.Item\>

        <MainMenu.Item\> Item 2 </MainMenu.Item\>

        <MobileFooter />

      </MainMenu\>

    </Excalidraw\>

  </div\>

);

// Need to render when code is span across multiple components

// in Live Code blocks editor

render(<App />);

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

[Edit this page](https://github.com/excalidraw/excalidraw/tree/master/dev-docs/docs/@excalidraw/excalidraw/api/children-components/footer.mdx)

[

Previous

Sidebar

](/docs/@excalidraw/excalidraw/api/children-components/sidebar)[

Next

LiveCollaborationTrigger

](/docs/@excalidraw/excalidraw/api/children-components/live-collaboration-trigger)