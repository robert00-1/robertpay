import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {loginUser} from "../../services/authService";
import useAuth from "../../hooks/useAuth";

export default function Login() {
    const navigate = useNavigate();

    const {login} = useAuth();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            setLoading(true);

            const data = await loginUser(
                email,
                password
            );

            login(data.access_token);

            navigate("/dashboard");
        } catch (error) {
            alert(
                error.response?.data?.detail ||
                "Login failed"
            );
        } finally {
            setLoading(false);
        }
    };

    return (
       <div className="min-h-screen bg-slate-100 flex items-center justify-center">
        <div className="w-full max-w-md bg-white rounded-xl shadow-lg p-8">
            <h1 className="text-3xl font-bold text-blue-600">
                RobertPay
            </h1>
            <p className="text-center text-gray-500 mt-2 mb-8">
                Merchant Dashboard
            </p>

            <form 
            onSubmit={handleSubmit}
            className="space-y-5"
            >
                <div>
                    <label className="font-medium">
                        Email
                    </label>

                    <input type="email"
                    className="w-full mt-2 border rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Enter email"
                    value={email}
                    onChange={(e) =>
                        setEmail(e.target.value)
                    }
                    required
                    />
                </div>
                <div
                
                >
                    <label className="font-medium">
                        Password
                    </label>
                    <input type="password"
                    className="w-full mt-2 border rounded-lg px-4 py-3 focus:outline-none focus:ring-2-blue-500"
                    placeholder="Enter password"
                    value={password}
                    onChange={(e) =>
                        setPassword(e.target.value)
                    }
                    required
                    />
                </div>

                <button
                className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg font-semibold"
                disabled={loading}
                >
                    {
                        loading
                        ? "Signing in..."
                        : "Sign In"
                    }


                </button>
            </form>
        </div>
       </div> 
    );
}