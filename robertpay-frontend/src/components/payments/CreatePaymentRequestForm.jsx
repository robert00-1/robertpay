import { useState } from "react";

const CreatePaymentRequestForm = ({ onSubmit, loading}) => {
    const [formData, setFormData] = useState({
        customer_name: "",
        customer_phone:"",
        customer_email:"",
        amount: "",
        reference: "",
        description: "",
    });

    const handleChange = (e) => {
        setFormData((prev) => ({
            ...prev,
            [e.target.name]: e.target.value,
        }));
    };
    const handleSubmit = (e) => {
        e.preventDefault();

        onSubmit({
            ...formData,
            amount: Number(formData.amount),
        });
        setFormData({
            customer_name:"",
            customer_phone: "",
            customer_email: "",
            amount: "",
            reference: "",
            description:"",
        });
    };

    return (
        <div className="bg-white rounded-xl shadow-md p-6">
            <h2 className="text-2xl font-bold mb-6">
                Initiate STK Push
            </h2>

            <form 
            onSubmit={handleSubmit}
            className="space-y-4"
            >
               <input type="text"
               name="customer_name"
               placeholder="Customer Name"
               value={formData.customer_name}
               onChange={handleChange}
               className="w-full border rounded-lg p-3"
               required
               /> 
               <input type="text"
               name="customer_phone"
               placeholder="2547XXXXXXXX"
               value={formData.customer_phone}
               onChange={handleChange}
               className="w-full border rounded-lg p-3"
               required
               />
               <input type="email"
               name="customer_email"
               placeholder="Customer Email (optional)"
               value={formData.customer_email}
               onChange={handleChange}
               className="w-full border rounded-lg p-3"
               />
               <input type="number"
               name="amount"
               placeholder="Amount"
               value={formData.amount}
               onChange={handleChange}
               className="w-full border rounded-lg p-3"
               required
               />
               <input type="text"
               name="reference"
               placeholder="Reference"
               value={formData.reference}
               onChange={handleChange}
               className="w-full border rounded-lg p-3"
               required
               />
               <textarea 
               name="description"
               placeholder="Description"
               value={formData.description}
               onChange={handleChange}
               className="w-full border rounded-lg p-3"
               rows={3}
               />
               <button
               type="submit"
               disabled={loading}
               className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 rounded"
               >
                {loading
                ? "Sending STK Push..."
                : "Initiate STK Push"
                }
               </button>
            </form>
        </div>
    );
};
export default CreatePaymentRequestForm;