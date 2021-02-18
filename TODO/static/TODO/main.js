
function Title(props){
    return(
        <h1>
        {props.name}
    </h1>
    )
        
}
function App(){
    const my_title="To-do List"
    return (
      <div>
      <Title name={my_title} />
      
    </div>
    )
  }
class Main extends React.Component{
    render(){
        return(
            <App/>
        )
    }
}

ReactDOM.render(<Main/>,document.getElementById('#app'))