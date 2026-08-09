import {
    Bell,
    UserCircle,
    Search,
} from "lucide-react";

const Navbar = () => {
    return (
        <header className="bg-white shadow-sm border-b px-8 py-5 flex items-center justiffy-between">


            <div>
                <h1 className="text-2xl font-bold text-gray-800">
                    Dashboard
                </h1>
                <p className="text-gray-500 text-sm">
                    Welcome to RobertPay
                </p>
            </div>

            <div className="hidden md:flex items-center">
                <div className="flex items-center bg-gray-100 rounded-lg px-4 py-2">
                    <Search 
                    size={18}
                    className="text-gray-400"
                    />
                    <input type="text"
                    placeholder="Search..."
                    className="bg-transparent outline-none ml-3"
                    />

                </div>
            </div>

            <div className="flex items-center gap-6"> 
                <button className="relative">
                    <Bell
                    size={24}
                    className="text-gray-600"
                    />
                    <span className="absolute -top-1 -right-1 h-3 w-3 bg-red-500 rounded-full"></span>
                </button>

                <div className="flex items-center gap-3">
                    <UserCircle
                    size={38}
                    className="text-green-600" />
                </div>

                <p className="font-semibold">
                    Robert Shop
                </p>
                <p className="text-sm text-gray-500">
                    Merchant
                </p>

            </div>
        </header>
    );
};
export default Navbar;