import {
    LayoutDashboard,
    CreditCard,
    Wallet,
    ArrowLeftRight,
    Settings,
    KeyRound,
    Receipt,
    LogOut,
    Code,
    
} from "lucide-react";

import { NavLink } from "react-router-dom";

const menuItems = [
    {
    name: "Dashboard",
    path: "/dashboard",
    icon: LayoutDashboard,
    },
    {
        name: "Payment Requests",
        path: "/payment-requests",
        icon: CreditCard,
    },
    
    

    {
        name: "Merchant Settings",
        path: "/settings",
        icon: Settings,
    },
    {
       name: "API Keys",
       path: "/dashboard/api-keys",
       icon: KeyRound, 
    },
    {
    name: "Developers",
    path: "/dashboard/developers",
    icon: Code
}
];

const Sidebar = () => {
    return (
        <aside className="w-72 min-h-screen bg-slate-900 text-white flex flex-col">
            <div className="px-8 py-8 border-b border-slate-700">
                <h1 className="text-3xl font-bold text-green-400">
                    RobertPay
                </h1>

                <p className="text-slate-400 text-sm mt-2">
                    Payment Platform
                </p>
            </div>
            <nav className="flex-1 mt-6">
                {menuItems.map((item) => {
                    const Icon = item.icon;

                    return (
                        <NavLink
                        key={item.name}
                        to={item.path}
                        className={({ isActive}) =>
                            `flex items-center gap-4 px-8 py-4 transition ${
                                isActive
                                ? "bg-green-600 text-white"
                                : "hover:bg-slate-800 text-slate-300"
                            }`
                        }
                        >
                            <Icon size={22} />

                            <span>{item.name}</span>
                        </NavLink>
                    );
                })}
            </nav>

            <div className="border-t border-slate-700 p-5">
                <button className="flex items-center gap-3 text-red-400 hover:text-red-300">
                    <LogOut size={20} />
                    Logout
                </button>
            </div>
        </aside>
    );
};
export default Sidebar;