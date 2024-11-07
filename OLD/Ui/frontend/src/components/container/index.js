import Label from "../content/label";
import Image from "../content/image";
import { useTranslation } from 'react-i18next';
import i18n from '../../translations/i18n'; 

export default function Container({ children }) {
    const { t } = useTranslation();

    const changeLanguage = (language) => {
        i18n.changeLanguage(language);
    };

    return (
        <div className="w-full flex items-center justify-center">
            <div className="w-[40%] h-screen">
                <div className="w-full mt-4 flex justify-end">
                    <div className=" flex w-24 gap-1 right-0">
                        <button onClick={() => changeLanguage('en')}><span>EN</span></button>
                        <button onClick={() => changeLanguage('fr')}><span>FR</span></button>
                        <button onClick={() => changeLanguage('de')}><span>DE</span></button>
                    </div>
                </div>
                <h1 className="text-4xl mt-12" id="title">{t('title')}</h1>
                <Image />
                <div className="w-full flex justify-center">
                    <div className="separator w-[75%] bg-black h-1"></div>
                </div>
                
                <Label />
                <div className="w-full flex justify-center mt-10">
                    <div className="h-12 text-center justify-center w-[75%] rounded-xl bg-lime-500">
                        <p className="p-3 text-xl">Start</p>
                    </div>
                </div>
            </div>
        </div>
    );
}
