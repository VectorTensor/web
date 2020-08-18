class Coefficents extends React.Component{
    render(){
        return(
                <div id="coef">
                     <input id="box" type="text" name={this.props.co}/>  {this.props.var}
                   
                </div>
                
                   
                
           


        );

    }
}

class Equation extends React.Component{
    render(){
        return(
           <div>
               
                

                <Coefficents var="x" co="a11"/> + a<Coefficents var="y" co="a12"/> + <Coefficents var="z" co="a13"/>=<Coefficents var="" co="a"/><br/>
                <Coefficents var="x" co="a21"/> + <Coefficents var="y" co="a22"/> + <Coefficents var="z" co="a23"/>=<Coefficents var="" co="b"/><br/>
                <Coefficents var="x" co="a31"/> + <Coefficents var="y" co="a32"/> + <Coefficents var="z" co="a33"/>=<Coefficents var="" co="c"/><br/>
                <input type="submit"/>

          

           </div>
                
                
            
              
        
            

        );
    }
}

class Rank extends React.Component{
    render(){
        return(
            <div>
                <Coefficents var="" co="a11"/>  <Coefficents var="" co="a12"/>  <Coefficents var="" co="a13"/><br/>
                <Coefficents var="" co="a21"/>  <Coefficents var="" co="a22"/>  <Coefficents var="" co="a23"/><br/>
                <Coefficents var="" co="a31"/>  <Coefficents var="" co="a32"/>  <Coefficents var="" co="a33"/>
                <input type="submit"/>
            </div>
        );
    }
}

class Eigen extends React.Component{
    render(){
        return(

            <div>
            <Coefficents var="" co="a11"/>  <Coefficents var="" co="a12"/>  <Coefficents var="" co="a13"/><br/>
            <Coefficents var="" co="a21"/>  <Coefficents var="" co="a22"/>  <Coefficents var="" co="a23"/><br/>
            <Coefficents var="" co="a31"/>  <Coefficents var="" co="a32"/>  <Coefficents var="" co="a33"/>
            <input type="submit"/>
        </div>
            
        );
    }
}


ReactDOM.render(<Equation/>,document.querySelector('#eqn'));
ReactDOM.render(<Rank/>,document.querySelector('#rank'));
ReactDOM.render(<Eigen/>,document.querySelector('#eigen'));