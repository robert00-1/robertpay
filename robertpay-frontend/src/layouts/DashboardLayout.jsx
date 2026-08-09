import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/layout/Navbar";

const DashboardLayout = ({ children }) => {
  return (
    <div className="flex bg-gray-100 min-h-screen">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Navbar />

        <main className="flex-1 p-8">
          {children}
        </main>

      </div>

    </div>
  );
};

export default DashboardLayout;