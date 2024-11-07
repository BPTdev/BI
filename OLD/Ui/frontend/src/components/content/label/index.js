import { useTranslation } from 'react-i18next';

export default function Image() {
    const { t } = useTranslation();

    return (
        <div className="w-full  flex justify-center mt-10">
            <div className="text-left p-3 w-[75%]">
                <h1 className="mb-4">{t('labels')}</h1>
                <div className="flex">
                    <div className="flex-1">
                        <p>Cat</p>
                        <p>Color</p>
                        <p>Animal</p>
                        <p>Car</p>
                        <p>House</p>
                    </div>
                    <div className="flex-1">
                        <p>89,543345</p>
                        <p>87,342562</p>
                        <p>78,323423</p>
                        <p>60,234823</p>
                        <p>60,134234</p>
                    </div>
                </div>
            </div>
        </div>
    );
    }