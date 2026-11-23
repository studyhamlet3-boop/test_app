import { useForm, type SubmitHandler } from 'react-hook-form'
import { apiFetch } from "../api/clients"
import './regist.css'

type FormData = {
  email: string;
  password: string;
  passwordRepeat: string;
};

function Regist() {
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>();

  const onSubmit: SubmitHandler<FormData> = async (data) => {

      let res: Response;
      try {
        res = await apiFetch("/auth/register", {
          method: "POST",
          credentials: "include",
          body: JSON.stringify({
          email: data.email,
          password: data.password
          })
        }, { redirectOnUnauthorized: true });
      }
      catch (error){
        console.error(error)
        return;
      }
      if (!res.ok) {
        console.error("Failed to fetch response");
        return;
      }
      else{
        window.location.href = "/";
      }
    

  }

  return (
    <>
    {/*  From Uiverse.io by rahilansari261  */}
    <form className="background" onSubmit={handleSubmit(onSubmit)}>
        <div className="htmlForm">
        <div className="title">Welcome</div>
        <div className="subtitle">Let's create your account!</div>

        <div className="input-container ic2">

            <input
            {...register("email", {
              required: "email is required",
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                message: "Invalid email address"
              }
            })}

            placeholder="" type="email"
            className="input"
            id="email"/>

            {errors.email && <span className="error">{errors.email.message}</span>}

            <div className="cut"></div>
            <label className="iLabel" htmlFor="email">Email</label>
        </div>
        <div className="input-container ic2">

            <input 
            {...register("password", {
              required: "password is required",
              minLength: {
                value: 6,
                message: "Password must be at least 6 characters"
              }
            })}
            placeholder=""
            type="password"
            className="input"
            id="password"
            />
            {errors.password && <span className="error">{errors.password.message}</span>}

            <div className="cut cut-short"></div>
            <label className="iLabel" htmlFor="password">Password</label>
        </div>
        <div className="input-container ic2">

            <input
            {...register("passwordRepeat", {
              required: "password is required",
              validate: (value, formValues) => value === formValues.password || "Passwords do not match"
            })}
            placeholder="" type="password"
            className="input"
            id="passwordRepeat"/>

            {errors.passwordRepeat && <span className="error">{errors.passwordRepeat.message}</span>}

            <div className="cut cut-short_passrep"></div>
            <label className="iLabel" htmlFor="passwordRepeat">Repeat Password</label>
        </div>
        <button className="submit" type="submit">submit</button>
        </div>
    </form>
    </>
  )
}

export default Regist
