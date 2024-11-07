import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

// Importez vos fichiers de langue ici. Par exemple :
import translationEN from './locales/en/translation.json';
import translationFR from './locales/fr/translation.json';
import translationDE from './locales/de/translation.json';

// Les ressources de traduction.
const resources = {
    en: {
        translation: translationEN
    },
    fr: {
        translation: translationFR
    },
    de: {
        translation: translationDE
    }
};

i18n
  .use(initReactI18next) // passe i18n down to react-i18next
    .init({
        resources,
        lng: "en", 
        keySeparator: false, // on utilise pas de clés en forme de phrases dans les fichiers de traduction
        interpolation: {
        escapeValue: false, // réagit déjà à l'échappement des valeurs
        }
    });

export default i18n;
