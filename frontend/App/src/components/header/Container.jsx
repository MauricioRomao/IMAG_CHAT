import './container.css'
const chat_img_login = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZ_pjVN_lNHy-4nnL4iZPbyu7loXaliB8VCA&usqp=CAU'
const Container = () => {
    return (
        <div className='container'>

            <div className="formulario">
                <form className="form_" method="get">
                    <input type="email" placeholder="Email" />
                    <br />
                    <input type="password" placeholder="Senha" />
                </form>
                <div className="page_function">
                    <button className="active" >Login</button>


                </div>

            </div>
            <div className="net_descr">
                <div className="social" >
                 <a href="#">Criar conta</a>
                    <div className="img_social">
                        <img src={chat_img_login} alt="image teste" />
                    </div>

                </div>
            </div>
        </div>
    )
}

export default Container