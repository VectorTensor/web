class Upload extends React.Component{
    render(){

        return (
        <div>
        <form>
            <h1>Add Question </h1>
            
        </form>
        
        </div>


        )


    }

}







class App extends React.Component{
    render(){
        return(
            <Upload/>
            
        );
    }
}
ReactDOM.render(<App/>,document.querySelector('#app'));
