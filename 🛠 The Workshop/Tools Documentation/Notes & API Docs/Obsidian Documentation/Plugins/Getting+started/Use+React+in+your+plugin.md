[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Use React in your plugin

In this guide, you'll configure your plugin to use [React](https://react.dev/). It assumes that you already have a plugin with a [custom view](https://docs.obsidian.md/Plugins/User+interface/Views) that you want to convert to use React.

While you don't need to use a separate framework to build a plugin, there are a few reasons why you'd want to use React:

*   You have existing experience of React and want to use a familiar technology.
*   You have existing React components that you want to reuse in your plugin.
*   Your plugin requires complex state management or other features that can be cumbersome to implement with regular [HTML elements](https://docs.obsidian.md/Plugins/User+interface/HTML+elements).

Configure your plugin
-----------------------

1.  Add React to your plugin dependencies:
    
        npm install react react-dom
        
    
2.  Add type definitions for React:
    
        npm install --save-dev @types/react @types/react-dom
        
    
3.  In `tsconfig.json`, enable JSX support on the `compilerOptions` object:
    
        {
          "compilerOptions": {
            "jsx": "react-jsx"
          }
        }
        
    

Create a React component
--------------------------

Create a new file called `ReactView.tsx` in the plugin root directory, with the following content:

    export const ReactView = () => {
      return <h4>Hello, React!</h4>;
    };
    

Mount the React component
---------------------------

To use the React component, it needs to be mounted on a [HTML elements](https://docs.obsidian.md/Plugins/User+interface/HTML+elements). The following example mounts the `ReactView` component on the `this.containerEl.children[1]` element:

    import { StrictMode } from "react";
    import { ItemView, WorkspaceLeaf } from "obsidian";
    import { Root, createRoot } from "react-dom/client";
    import { ReactView } from "./ReactView";
    
    const VIEW_TYPE_EXAMPLE = "example-view";
    
    class ExampleView extends ItemView {
    	root: Root | null = null;
    
    	constructor(leaf: WorkspaceLeaf) {
    		super(leaf);
    	}
    
    	getViewType() {
    		return VIEW_TYPE_EXAMPLE;
    	}
    
    	getDisplayText() {
    		return "Example view";
    	}
    
    	async onOpen() {
    		this.root = createRoot(this.containerEl.children[1]);
    		this.root.render(
    			<StrictMode>
    				<ReactView />,
    			</StrictMode>,
    		);
    	}
    
    	async onClose() {
    		this.root?.unmount();
    	}
    }
    

For more information on `createRoot` and `unmount()`, refer to the documentation on [ReactDOM](https://react.dev/reference/react-dom/client/createRoot#root-render).

You can mount your React component on any `HTMLElement`, for example [status bar items](https://docs.obsidian.md/Plugins/User+interface/Status+bar). Just make sure to clean up properly by calling `this.root.unmount()` when you're done.

Create an App context
-----------------------

If you want to access the [App](https://docs.obsidian.md/Reference/TypeScript+API/App) object from one of your React components, you need to pass it as a dependency. As your plugin grows, even though you're only using the `App` object in a few places, you start passing it through the whole component tree.

Another alternative is to create a React context for the app to make it globally available to all components inside your React view.

1.  Use `createContext()` to create a new app context.
    
        import { createContext } from "react";
        import { App } from "obsidian";
        
        export const AppContext = createContext<App | undefined>(undefined);
        
    
2.  Wrap the `ReactView` with a context provider and pass the app as the value.
    
        this.root = createRoot(this.containerEl.children[1]);
        this.root.render(
          <AppContext.Provider value={this.app}>
            <ReactView />
          </AppContext.Provider>
        );
        
    
3.  Create a custom hook to make it easier to use the context in your components.
    
        import { useContext } from "react";
        import { AppContext } from "./context";
        
        export const useApp = (): App | undefined => {
          return useContext(AppContext);
        };
        
    
4.  Use the hook in any React component within `ReactView` to access the app.
    
        import { useApp } from "./hooks";
        
        export const ReactView = () => {
          const { vault } = useApp();
        
          return <h4>{vault.getName()}</h4>;
        };
        
    

For more information, refer to the React documentation for [Passing Data Deeply with Context](https://react.dev/learn/passing-data-deeply-with-context) and [Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks).

Use React in your plugin

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)